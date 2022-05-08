# **Job scraping with Python and Docker**
---
This application searches for job postings by a given job title and performs an NLP analysis to find the most commonly mentioned skills and qualifications in job listings. The results are saved to a postgres database and displayed in a dash plotly dashboard.


## Structure of the project
---
![architecture](markupObj/architecture.png)
---
## How to start the application
---
As prerequisits docker-cli (docker-desktop on Windows) and docker-compose have to be installed. See also https://www.docker.com for further instructions.

- todo: table of commands and description.
| Description: | start build process |
| --- |---:|
| Command: | docker-compose up --build |

## Known issues
---
This application is a prototype and subject to continuous improvement. 

A common issue is that the 'dashboard' container does not wait for the 'app' container to finish. Therefore some diagramms can remain empty.
_Workaround: 