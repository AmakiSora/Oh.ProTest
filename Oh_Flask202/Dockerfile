FROM python:3.9
MAINTAINER cosmos
WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py /usr/src/app/app.py

ENTRYPOINT [ "python", "./app.py" ]
EXPOSE 8000