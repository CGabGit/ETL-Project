import dbConnection
import fetchJobSearch
import fetchJobItem
import time
import os

dbConnection.waitForPostgresContainer()
fetchJobSearch.extractData()
fetchJobItem.extractData()