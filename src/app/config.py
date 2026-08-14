import json
import os
from pathlib import Path
from typing import Any


class Config:
    """Application configuration loader."""

    def __init__(self, config_path: str | Path) -> None:
        self._config = self._load_config(config_path)

    def get(self, key: str, default: Any = None) -> Any:
        """
        Get a configuration value, preferring environment variables.
        """
        return os.getenv(key, self._config.get(key, default))

    @staticmethod
    def _load_config(config_path: str | Path) -> dict[str, Any]:
        """
        Load configuration values from a JSON file when running locally.
        """
        environment = os.getenv("ENVIRONMENT", "local")

        if environment == "local":
            path = Path("config.json")
        else:
            path = Path(config_path)

        if not path.exists():
            raise FileNotFoundError(f"Configuration file not found: {path}")

        with path.open("r", encoding="utf-8") as config_file:
            return json.load(config_file)
