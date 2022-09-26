import os

from flask import Flask

from sample.celery import create_celery


def create_app() -> Flask:
    app = Flask(__name__)
    app.config["CELERY_RESULT_BACKEND"] = os.getenv("CELERY_RESULT_BACKEND")
    app.config["CELERY_BROKER_URL"] = os.getenv("CELERY_BROKER_URL")

    @app.get("/healthcheck")
    def healthcheck():
        return "OK"

    return app


celery_app = create_celery(create_app())
