import logging
import typing as t
import time
from threading import Thread

logger = logging.getLogger(__name__)


CHECK_INTERVAL = 5.0


class Supervisor:
    """Monitors consumer threads and logs when one stops."""

    def __init__(
        self,
        consumer_threads: t.Collection[Thread],
    ) -> None:
        self.consumer_threads = consumer_threads

    def monitor(self) -> None:
        """Monitor consumer threads until the supervisor is stopped."""
        while True:
            self._check_threads()
            time.sleep(CHECK_INTERVAL)

    def _check_threads(self) -> None:
        """Check whether all consumer threads are alive."""
        for thread in self.consumer_threads:
            if not thread.is_alive():
                logger.error(
                    "Consumer thread '%s' is no longer alive.",
                    thread.name,
                )


def start_threads(
    consumers: t.Collection[Consumer], config: Config
) -> t.Collection[Thread]:
    consumer_threads = [
        Thread(
            target=consumer.consume,
            name=f"consumer-{consumer.queue_name}",
        )
        for consumer in config.get("consumers")
    ]

    for thread in consumer_threads:
        thread.start()

    return consumer_threads
