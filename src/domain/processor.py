import json
from typing import Any

from src.domain.exceptions import ParserException

WRITE_OPERATION_TYPE = "read"
UPDATE_OPERATION_TYPE = "update"
OPERATION_TYPES = frozenset(WRITE_OPERATION_TYPE, UPDATE_OPERATION_TYPE)


class MessageParser:
    """
    Parser class for parsing messages from RabbitMQ.

    Expected message:
    {
        "operation": "read",
        "params": {...}
    }
    """

    def parse(self, message: str) -> tuple(str, str):
        """
        Parse and validate the message from RabbitMQ.
        """
        try:
            parsed_message = json.loads(message)
        except json.JSONDecodeError as exc:
            raise ParserException("The incoming message is not valid JSON") from exc

        if not isinstance(parsed_message, dict):
            raise ParserException("The incoming message must be a JSON object")

        required_fields = {"operation", "params"}

        if not required_fields.issubset(parsed_message):
            raise ParserException("The incoming message is missing required fields")

        operation = parsed_message["operation"]

        if operation not in self._OPERATION_TYPES:
            raise ParserException(f"Invalid operation type: {operation}")

        return (operation, params)


class MessageProcessor:
    """
    Processor class for processing messages from RabbitMQ.
    """

    def __init__(self, message: str) -> None:
        self.parser = MessageParser()
        self.message = message

    def parse(self) -> tuple(str, str):
        return self.parser.parse(self.message)
