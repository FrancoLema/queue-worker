import json
from typing import Any

from domain.exceptions import ParserException

WRITE_OPERATION_TYPE = "read"
UPDATE_OPERATION_TYPE = "update"
OPERATION_TYPES = frozenset((WRITE_OPERATION_TYPE, UPDATE_OPERATION_TYPE))


class MessageParser:
    """
    Parser class for parsing messages from RabbitMQ.

    Expected message:
    {
        "operation": "read",
        "params": {...}a
    }
    """

    def parse_message(self, message: str) -> dict:
        return self._parse(message)

    def _parse(self, message: str) -> dict:
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

        return parsed_message
