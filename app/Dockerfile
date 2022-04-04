FROM python:3.8
WORKDIR /code
ADD requirements.txt requirements.txt
RUN pip --no-cache-dir install -r requirements.txt
RUN python -m nltk.downloader punkt
COPY dbConnection.py dbConnection.py
COPY etlPrjMain.py etlPrjMain.py
COPY fetchJobSearch.py fetchJobSearch.py
COPY fetchJobItem.py fetchJobItem.py
COPY scraper.py scraper.py
COPY nlpModule.py nlpModule.py
CMD ["python", "-u", "etlPrjMain.py"]