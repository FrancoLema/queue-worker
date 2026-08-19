from .worker import Worker
from celery import Celery
from app.config import Config

config = Config()

celery_app = Celery(
    "project",
    broker=config.get("internal_broker"),
)


@celery_app.task
def process_message(message, worker):
    worker.process(message)
