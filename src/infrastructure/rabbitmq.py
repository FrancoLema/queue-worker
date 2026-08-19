import pika


def create_queue(queue_name: str) -> None:
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host="rabbitmq",
            port=5672,
        )
    )

    try:
        channel = connection.channel()

        channel.queue_declare(
            queue=queue_name,
            durable=True,
        )
    finally:
        connection.close()
