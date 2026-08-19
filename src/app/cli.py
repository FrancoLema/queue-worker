import typer

from infrastructure.rabbitmq import create_queue
from infrastructure.worker import Worker

app = typer.Typer()


@app.command()
def queue(queue_name: str = "messages") -> None:
    """Create the RabbitMQ queue."""
    create_queue(queue_name)


@app.command()
def worker() -> None:
    worker = Worker()


if __name__ == "__main__":
    app()
