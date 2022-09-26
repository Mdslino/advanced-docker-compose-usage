FROM python:3.10.7-slim-bullseye

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends curl apt-utils && \
    rm -rf /var/lib/apt/lists/*

RUN pip install poetry && poetry config virtualenvs.create false

COPY poetry.lock pyproject.toml ./

RUN poetry install

COPY . .

EXPOSE 8000