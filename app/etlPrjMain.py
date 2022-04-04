import dbConnection
import fetchJobSearch
import time
import os

dbConnection.waitForPostgresContainer()
fetchJobSearch.extractData()
