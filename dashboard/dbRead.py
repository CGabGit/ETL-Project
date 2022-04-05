import psycopg2
import time 
from sqlalchemy import create_engine
import sqlalchemy
import pandas as pd

# Database credentials
db_name = 'stepstone'
db_user = 'postgres'
db_pass = 'docker'
db_host = 'db' # service-name acordingly to docker-compose.yml 
db_port = '5432'

#db_string = "postgresql://postgres:docker@db:5432/stepstone"
db_string = f'postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'
db = create_engine(db_string)

def openDBConnection():
    connection = psycopg2.connect(
        host= db_host,
        port= db_port,
        user= db_user,
        password= db_pass,
        database= db_name)
    return connection

def closeDBConnection(connection):
    connection.close()

def getEngine():
    # connection string: driver://username:password@server/database
    db_string = f'postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'
    engine = sqlalchemy.create_engine(db_string)
    return engine

# def waitForScraperApp():
#     while True:
#         try:
#             connection = openDBConnection()
#             cursor = connection.cursor()
#             row_exists = f"""
#             SELECT EXISTS(SELECT 1 FROM tbl_status WHERE is_finnished = 1 )
#             """
#             cursor.execute(row_exists)
#             closeDBConnection(connection)
#             break
#         except:
#             print("wait for webscraping to finish...")
#             time.sleep(30)

def waitForScraperApp():
    row = 0
    while row != 1:
        try:
            connection = openDBConnection()
            cursor = connection.cursor()
            row = f"""
            SELECT 1 FROM tbl_status
            """
            cursor.execute(row)
            closeDBConnection(connection)
            break
        except:
            print("wait for webscraping to finish...")
            time.sleep(5)


def loadTblNumResFound(table_name):
    engine = getEngine()
    tblNumResultsFound = pd.read_sql(f'SELECT * FROM {table_name}', engine)
    return tblNumResultsFound

def loadTblWordFreq(table_name):
    engine = getEngine()
    tblWordFreq = pd.read_sql(f'SELECT * FROM {table_name}', engine)
    return tblWordFreq

def loadTblJI():
    engine = getEngine()
    jobItems = pd.read_sql('SELECT * FROM tbl_jobitems', engine)
    return jobItems