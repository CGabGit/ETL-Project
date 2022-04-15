import dbConnection
import fetchJobSearch
import fetchJobItem
import nlpModule
import time
import os

dbConnection.waitForPostgresContainer()
fetchJobSearch.extractData()
fetchJobItem.extractData()
nlpModule.preprocessing()
