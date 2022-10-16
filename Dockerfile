FROM python:3.9-slim-buster

COPY . /usr/src/app
WORKDIR /usr/src/app
RUN apt-get update
RUN pip install poetry
RUN poetry config virtualenvs.create false --local
RUN poetry install
RUN pytest

WORKDIR /usr/src/app/reply_insta_classifier

RUN useradd -ms /bin/bash serviceuser
USER serviceuser

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]