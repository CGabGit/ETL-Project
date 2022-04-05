FROM python:3.8
WORKDIR /dashboard
ADD requirements.txt requirements.txt
ENV DASH_DEBUG_MODE True
COPY plotlyapp.py plotlyapp.py
COPY dbRead.py dbRead.py
RUN set -ex && \
    pip install -r requirements.txt
EXPOSE 8050
CMD ["python", "plotlyapp.py"]