from dataclasses import dataclass
from datetime import datetime
from typing import Any


@dataclass
class Task:
    tracking_id: str
    status: str
    result: Any | None = None
    error: str | None = None
    start_time: datetime | None = None
    end_time: datetime | None = None

    def start(self) -> None:
        self.status = "running"
        self.start_time = datetime.now()

    def complete(self, result: Any) -> None:
        self.status = "completed"
        self.result = result
        self.end_time = datetime.now()

    def fail(self, error: str) -> None:
        self.status = "failed"
        self.error = error
        self.end_time = datetime.now()
