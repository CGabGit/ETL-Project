"""
In 'dbConnection.py' all database related CRUD commands 
are defined
"""

import psycopg2
import time 
from sqlalchemy import create_engine

# Database credentials
db_name = 'stepstone'
db_user = 'postgres'
db_pass = 'docker'
db_host = 'db' # service-name acordinglz to docker-compose.yml 
db_port = '5432'

#db_string = "postgresql://postgres:docker@db:5432/stepstone"
db_string = f'postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'
db = create_engine(db_string)

def waitForPostgresContainer():
    while True:
        try:
            con = openDBConnection()
            closeDBConnection(con)
            break
        except:
            print("wait for database system...")
            time.sleep(1)

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

def rowExists(job_id):
    connection = openDBConnection()
    cursor = connection.cursor()
    row_exists = f"""
    SELECT EXISTS(SELECT 1 FROM tbl_searchresults WHERE job_id = '{job_id}' )
    """
    cursor.execute(row_exists)
    duplicate_bool = cursor.fetchone()
    if duplicate_bool[0] == True:
        print(f"Row {job_id} already exists!")
        return True
    else: 
        return False

def insertToTblSR(connection, jobList, tableName):
    job_id = jobList[0].replace("'","")
    job_title = jobList[1].replace("'","")
    job_link = jobList[2].replace("'","")
    timestamp = jobList[3].replace("'","")
    cursor = connection.cursor()

    row_exists = f"""
    SELECT EXISTS(SELECT 1 FROM tbl_searchresults WHERE job_id = '{job_id}' )
    """
    cursor.execute(row_exists)
    duplicate_bool = cursor.fetchone()
    if duplicate_bool[0] == False:
        sql = f"""
        INSERT INTO {tableName}(job_id, job_title, job_link, date_scraped)
        values('{job_id}', '{job_title}', '{job_link}','{timestamp}')
        """
        cursor.execute(sql)
        connection.commit()

def insertToTblNumResFnd(connection, resultsFound, tableName):
    timestamp = resultsFound[0].replace("'","")
    searchTerm = resultsFound[1].replace("'","")
    maxSearchResults = resultsFound[2]

    cursor = connection.cursor()

    sql = f"""
    INSERT INTO {tableName}(daterecoded, searchterm, searchresults)
    values('{timestamp}', '{searchTerm}', '{maxSearchResults}')
    """
    cursor.execute(sql)
    connection.commit()

def insertToTblJobItems():
    pass

def truncateData():
    pass

def getEngine():
    pass

def loadTblSr():
    pass

def loadTblWordFreq():
    pass

def loadTblNumFound():
    pass


def insertWordFreq():
    pass