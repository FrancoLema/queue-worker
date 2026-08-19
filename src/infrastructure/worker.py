import logging
from queue import Queue
from threading import Thread
from typing import Any

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)


class Worker:
    """
    This worker only processes operations types defined in domain/processor OPERATION_TYPES

    TODO: implement celery task for receiving the consumer task in this class.
    """

    def __init__(
        self,
    ) -> None:
        pass

    def process(self, message: dict[str, Any]) -> None:
        try:
            logger.info("Task executed successfully")
        except Exception as exc:
            raise Exception("An error has ocurred during the process: ", exc)
