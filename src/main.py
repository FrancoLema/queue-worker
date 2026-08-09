from fastapi import FastAPI

app = FastAPI(
    title="queue-worker",
    description=(
        "Application for spinning up RabbitMQ queue consumers "
        "and sending received messages for processing."
    ),
    version="0.1.0",
)