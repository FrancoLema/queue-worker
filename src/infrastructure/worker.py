import logging
from queue import Queue
from threading import Thread
from typing import Any
from src.domain.processor import MessageProcessor, OPERATION_TYPES
from src.domain.tasks import Task

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
        queue: Queue[dict[str, Any]],
        processor: MessageProcessor,
        repository: TaskRepository,
    ) -> None:
        self.queue = queue
        self.processor = MessageProcessor
        self.repository = repository

    def process(self, message: dict[str, Any]) -> Task:
        try:
            operation = self.processor.parse(message)
            logger.info("Task executed successfully")
        except Exception as exc:
            raise Exception("An error has ocurred during the process: ", exc)

    def _do_operation(self, operation: tuple) -> None:
        operation_type = operation[0]
        params = operation[1]
        if operation_type in OPERATION_TYPES:
            if operation_type == WRITE_OPERATION_TYPE:
                return self.repository.create(params)
            if operation_type == UPDATE_OPERATION_TYPE:
                return self.repository.update(params)
