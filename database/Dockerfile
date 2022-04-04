FROM postgres:14.1-alpine
ENV POSTGRES_PASSWORD docker
ENV POSTGRES_DB stepstone
COPY stepstone.sql /docker-entrypoint-initdb.d/stepstone.sql