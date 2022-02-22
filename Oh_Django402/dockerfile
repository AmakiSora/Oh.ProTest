FROM python:3.9
MAINTAINER cosmos
WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY helloworld /usr/src/app/helloworld
COPY Oh_Django402 /usr/src/app/Oh_Django402
COPY db.sqlite3 /usr/src/app/db.sqlite3
COPY manage.py /usr/src/app/manage.py

ENTRYPOINT [ "python", "manage.py","runserver","0.0.0.0:8000" ]
EXPOSE 8000