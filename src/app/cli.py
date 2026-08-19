import typer

from infrastructure.rabbitmq import create_queue
from infrastructure.worker import Worker
from consumer.consumer import Consumer

app = typer.Typer()


@app.command()
def worker() -> None:
    worker = Worker()


@app.command()
def consumer(queue_name: str = "messages") -> None:
    consumer = Consumer(queue_name=queue_name)
    consumer.consume()


if __name__ == "__main__":
    app()
