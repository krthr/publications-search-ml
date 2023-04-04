FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11
ENV APP_MODULE app.api:app
ENV LOG_LEVEL debug
ENV WEB_CONCURRENCY 2

COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY ./scripts   /app/app/scripts
COPY ./app /app/app

RUN python /app/app/scripts/download_model.py
