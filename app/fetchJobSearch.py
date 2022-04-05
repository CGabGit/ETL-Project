'''
fetchJobSearch.py' conducts a search on www.stepstone.de 
for a given search-term and scrapes all url's of all  
job-listing and saves it to Posgres
'''

import requests
from bs4 import BeautifulSoup
import re
import time
import dbConnection
from datetime import datetime
from random import randrange
import pandas as pd
import scraper

def extractData():
    googleSpreadsheet = "https://docs.google.com/spreadsheets/d/1tUgxvygQ_iykSaM5T2rVjK2DViuWpWAl0I_Y1e7yDfE/export?format=csv"
    dataframe = pd.read_csv(googleSpreadsheet)
    for i,row in dataframe.iterrows():
        searchTerm = row[0]
        maxResults = row[1]

        # # base request
        # resp = requests.get('https://www.stepstone.de/',
        #                 headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36','accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'en-US,en;q=0.9','accept-encoding': 'gzip, deflate, br','sec-fetch-mode': 'navigate','sec-fetch-dest': 'document','upgrade-insecure-requests':'1'})
        # cookies_dict = resp.cookies
        cookies_dict = scraper.setCookieRequest('https://www.stepstone.de/')

        # scrape max number of search results
        numberOfResultsFound(searchTerm, cookies_dict)

        for page in range(0,maxResults,25):
            url = f'https://www.stepstone.de/5/ergebnisliste.html?what={searchTerm}&of={page}'
            # request with cookies
            # r = requests.get(url,cookies = cookies_dict,
            #                     headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
            #                             'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            #                             'accept-language': 'en-US,en;q=0.9',
            #                             'upgrade-insecure-requests': '1',
            #                             'sec-fetch-dest' : 'document',
            #                             'sec-fetch-mode' : 'navigate',
            #                             'sec-fetch-site': 'none'})
            r = scraper.scrapeRequest(url, cookies_dict)
            soup = BeautifulSoup(r.content, 'html.parser')
            print(transform(soup))

            time.sleep(randrange(62,82))

def transform(soup):
    connection = dbConnection.openDBConnection()
    divs = soup.find('div', re.compile("^ResultsSectionContainer"))
    for i in divs.find_all('article'):
        job_id = i['id']
        job_id = job_id[9:]
        job_title = i.h2.text.strip()
        job_link = i.find('a', {'data-at': 'job-item-title'})['href']
        timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")

        # call Postgres:
        joblist = [job_id,job_title,job_link,timestamp]
        dbConnection.insertToTblSR(connection, joblist, "tbl_searchresults")

    dbConnection.closeDBConnection(connection)
    return "job listings saved to DB"

def numberOfResultsFound(searchTerm, cookies_dict):
    connection = dbConnection.openDBConnection()
    url = f'https://www.stepstone.de/5/ergebnisliste.html?what={searchTerm}&of=0'
    # # request with cookies
    # r = requests.get(url,cookies = cookies_dict,
    #                     headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
    #                             'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    #                             'accept-language': 'en-US,en;q=0.9',
    #                             'upgrade-insecure-requests': '1',
    #                             'sec-fetch-dest' : 'document',
    #                             'sec-fetch-mode' : 'navigate',
    #                             'sec-fetch-site': 'none'})
    r = scraper.scrapeRequest(url, cookies_dict)
    
    soup = BeautifulSoup(r.content, 'html.parser')
    span = soup.find('span',"at-facet-header-total-results")

    maxSearchResults = span.text
    maxSearchResults = maxSearchResults.replace('.','')
    maxSearchResults = int(maxSearchResults)

    timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")

    resultsFound = [timestamp,searchTerm,maxSearchResults]
    dbConnection.insertToTblNumResFnd(connection, resultsFound, "tbl_numresultsfound")
    dbConnection.closeDBConnection(connection)
    return print(str(maxSearchResults) +" JobAds found for SearchTerm: "+searchTerm)



