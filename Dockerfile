FROM python:3.11-slim as builder

WORKDIR /app

RUN apt-get update
RUN apt install -y git

COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt


FROM builder as container

COPY ./scripts ./scripts
COPY ./app ./app

RUN pwd
RUN python /app/scripts/download_model.py
RUN ls -alh ~/.cache/clip

RUN ls -alh

CMD uvicorn app.api:app --host 0.0.0.0 --port $PORT --log-level debug --workers 1
