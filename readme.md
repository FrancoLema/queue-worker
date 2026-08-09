# queue-worker

Application for spinning up RabbitMQ queue consumers and sending received messages for processing.

## Requirements

- Python 3.12+
- [Poetry](https://python-poetry.org/)

## Installation

```bash
poetry install
```

## Usage

```bash
poetry run uvicorn src.main:app --reload
```

## License

MIT
