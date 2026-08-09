class MessageParser:
    """
    Parser class for parsing messages from RabbitMQ.
    """

    def __init__(self, message: str):
        self.message = message

    def parse(self) -> dict:
        """
        Parse the message from RabbitMQ.
        """
        return json.loads(self.message)


class MessageProcessor:
    """
    Parser class for parsing messages from RabbitMQ.
    """

    def __init__(self, message: str):
        self.parser = MessageParser()
        self.message = message

    def parse(self) -> dict:
        """
        Parse the message from RabbitMQ.
        """
        return json.loads(self.message)
