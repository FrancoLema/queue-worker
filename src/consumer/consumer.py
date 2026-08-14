import logging

import pika
from pika.adapters.blocking_connection import BlockingChannel

logger = logging.getLogger(__name__)


class Consumer:
    """Consumer for a RabbitMQ queue."""

    def __init__(self, queue_name: str, worker: Worker) -> None:
        self.queue_name = queue_name
        self.worker = worker

    def consume(self) -> None:
        """Consume messages from RabbitMQ."""
        connection = self._connect()
        channel = connection.channel()

        channel.queue_declare(
            queue=self.queue_name,
            durable=True,
        )

        channel.basic_consume(
            queue=self.queue_name,
            on_message_callback=self._handle_message,
            auto_ack=False,
        )

        logger.info("Consumer started for queue '%s'", self.queue_name)

        try:
            channel.start_consuming()
        except Exception:
            logger.exception(
                "Error consuming messages from queue '%s'",
                self.queue_name,
            )
            raise
        finally:
            if connection.is_open:
                connection.close()

    def _connect(self) -> pika.BlockingConnection:
        """Connect to RabbitMQ with up to three attempts."""
        for attempt in range(1, 4):
            try:
                logger.info(
                    "Connecting to RabbitMQ. Attempt %d/3",
                    attempt,
                )

                return pika.BlockingConnection(
                    pika.ConnectionParameters(
                        host="localhost",
                        port=5672,
                    )
                )

            except pika.exceptions.AMQPConnectionError:
                logger.exception(
                    "Failed to connect to RabbitMQ. Attempt %d/3",
                    attempt,
                )

        raise ConnectionError(
            f"Could not connect to RabbitMQ after 3 attempts "
            f"for queue '{self.queue_name}'"
        )

    def _handle_message(
        self,
        channel: BlockingChannel,
        method: pika.spec.Basic.Deliver,
        properties: pika.BasicProperties,
        body: bytes,
    ) -> None:
        """Delegate the message to the worker."""
        try:
            logger.info("Message received from queue '%s'", self.queue_name)

            self.worker.process(body)

            channel.basic_ack(
                delivery_tag=method.delivery_tag,
            )
        except Exception:
            logger.exception(
                "Error processing message from queue '%s'",
                self.queue_name,
            )

            channel.basic_nack(
                delivery_tag=method.delivery_tag,
                requeue=False,
            )
