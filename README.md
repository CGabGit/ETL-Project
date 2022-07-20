# **Job scraping with Python and Docker**
---
This application searches for *job postings* by a given *job title* and performs a *NLP analysis* to find the most commonly mentioned skills and qualifications in job listings. The results are saved to a postgres database and displayed in a dash plotly dashboard.


## Structure of the project
---
![architecture](markupObj/architecture.png)
---
## Main packages used
---
| **web scraping** | **HTML Parser** | **extract data** | **database driver** | **NLP**              | **dashboard**     |
|------------------|-----------------|------------------|---------------------|----------------------|-------------------|
| beautifulSoup 4  | html5lib        | regex            | psycopg2            | NLTK                 | dash              |
| requests         | lxml            | json             | SQLAlchemy          | NLTK 'punkt package' | plotly.graph_objs |
| requests-html    |                 | pandas           |                     |                      |                   |

---
## How to start the application
---
Prerequisits: docker-cli (docker-desktop on Windows) and docker-compose have to be installed. See also https://www.docker.com for further instructions.

Please notice:
- All docker-compose commands can only be executed in the root directory of the project where 'docker-compose.yml' is located!
- The performance of the web scraping module is configured to ensure a fair and responsible use of publicly available website resources.


start-up with build process
```bash
docker-compose up --build
```

| Description: | start-up in background                                            |
| Command:     | docker-compose up -d                                              |
|              |                                                                   |
| Description: |  shutdown                                                         |
| Command:     | docker-compose down                                               |
|              |                                                                   |
| Description: |  display all running containers                                   |
| Command:     | docker ps                                                         |
|              |                                                                   |
| Description: |  display running & stopped containers                             |
| Command:     | docker ps -a                                                      |
|              |                                                                   |
| Description: |  display all images                                               |
| Command:     | docker images                                                     |
|              |                                                                   |
| Description: |  log on to docker-compose container with service name 'db'        |
| Command:     | docker-compose exec db sh                                         |
|              |                                                                   |
| Description: |  switch to root-user                                              |
| Command:     | su -                                                              |
|              |                                                                   |
| Description: |  log-in to postgres database called 'stepstone' & user 'postgres' |
| Command:     | psql -d stepstone -U postgres                                     |
|              |                                                                   |
| Description: |  display all tables of the database                               |
| Command:     | \dt                                                               |
|              |                                                                   |
| Description: |  display content of table 'tbl_bigrams'                           |
| Command:     | SELECT * FROM tbl_bigrams;                                        |
|              |                                                                   |
| Description: |  stop the 'dashboard' service(container)                          |
| Command:     | docker-compose stop dashboard                                     |
|              |                                                                   |
| Description: |  start the 'dashboard' service(container)                         |
| Command:     | docker-compose start dashboard                                    |

|              |                                                                   |
|--------------|-------------------------------------------------------------------|
| Description: |  start-up with build process                                      |
| Command:     | docker-compose up --build                                         |
|              |                                                                   |
| Description: | start-up in background                                            |
| Command:     | docker-compose up -d                                              |
|              |                                                                   |
| Description: |  shutdown                                                         |
| Command:     | docker-compose down                                               |
|              |                                                                   |
| Description: |  display all running containers                                   |
| Command:     | docker ps                                                         |
|              |                                                                   |
| Description: |  display running & stopped containers                             |
| Command:     | docker ps -a                                                      |
|              |                                                                   |
| Description: |  display all images                                               |
| Command:     | docker images                                                     |
|              |                                                                   |
| Description: |  log on to docker-compose container with service name 'db'        |
| Command:     | docker-compose exec db sh                                         |
|              |                                                                   |
| Description: |  switch to root-user                                              |
| Command:     | su -                                                              |
|              |                                                                   |
| Description: |  log-in to postgres database called 'stepstone' & user 'postgres' |
| Command:     | psql -d stepstone -U postgres                                     |
|              |                                                                   |
| Description: |  display all tables of the database                               |
| Command:     | \dt                                                               |
|              |                                                                   |
| Description: |  display content of table 'tbl_bigrams'                           |
| Command:     | SELECT * FROM tbl_bigrams;                                        |
|              |                                                                   |
| Description: |  stop the 'dashboard' service(container)                          |
| Command:     | docker-compose stop dashboard                                     |
|              |                                                                   |
| Description: |  start the 'dashboard' service(container)                         |
| Command:     | docker-compose start dashboard                                    |

## Dashboard
---
The dashboard can be accessed on:
*127.0.0.1:8050*


![linechart](markupObj/linechart.png)\
*Example 1:* Time series with count of job postings for job title 'Wirtschaftsinformatiker' 

![onegrams_barchart](markupObj/barchart_onegrams.png)\
*Example 2:* unigrams found for job title 'Wirtschaftsinformatiker' 

![bigrams_barchart](markupObj/bigrams_barchart.png)\
*Example 3:* Bigrams found for job title 'Wirtschaftsinformatiker'

## Configuation and download of data
---
The search term itself, the maximum number of search results used for the analysis, raw data of db-tables as well as the lists of stop words for unigrams, bigrams and trigrams can be accessed through the dashboard.\ 
In this version the stop word lists are integrated via google sheets.

![default stopwords](markupObj/default_german_stopwords.png)\
*Example 4:* Customizable german stopword sheet.

## Known issues
---
This application is a prototype and subject to continuous improvements.
A common issue is that the 'dashboard' container does not wait for the 'app' container to finish. Therefore some diagramms can remain empty.
Workaround: at the time the NLP analysis is done, stop the 'dashboard' service and start the 'dashboard' service again. 

Please also see 'Issues' section of this repo. 
