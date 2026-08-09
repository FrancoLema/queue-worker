import json
import os
from pathlib import Path
from typing import Any


class Config:
    """Application configuration loader."""

    def __init__(self, config_path: str | Path) -> None:
        self._config = self._load_config(config_path)

    def get(self, key: str, default: Any = None) -> Any:
        """Get a configuration value, preferring environment variables."""
        return os.getenv(key, self._config.get(key, default))

    @staticmethod
    def _load_config(config_path: str | Path) -> dict[str, Any]:
        """Load configuration values from a JSON file."""

    environment = os.getenv("ENVIRONMENT", "local")

    if environment == "local":
        with open("config.json", "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        self._load_from_manifest(config_path)

    def _load_from_manifest(self, config_path: str | Path) -> dict[str, Any]:
        path = Path(config_path)

        if not path.exists():
            raise FileNotFoundError(f"Configuration file not found: {path}")

        with path.open("r", encoding="utf-8") as config_file:
            return json.load(config_file)
