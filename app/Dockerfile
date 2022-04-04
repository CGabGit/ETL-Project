FROM python:3.8
WORKDIR /code
ADD requirements.txt requirements.txt
RUN pip --no-cache-dir install -r requirements.txt
COPY dbConnection.py dbConnection.py
COPY etlPrjMain.py etlPrjMain.py
COPY fetchJobSearch.py fetchJobSearch.py
COPY scraper.py scraper.py
CMD ["python", "-u", "etlPrjMain.py"]