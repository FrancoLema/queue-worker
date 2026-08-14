from sqlalchemy.orm import Session

from domain.task import Task
from infrastructure.Repository.tasks import TaskModel


class TaskRepository:
    """
    Repository for the Task model.
    """

    _TABLE_NAME = "tasks"

    def __init__(self, db: Session) -> None:
        self.db = db

    def _to_domain_task(self, task: TaskModel) -> Task:
        return Task(
            tracking_id=task.tracking_id,
            status=task.status,
            result=task.result,
            error=task.error,
            start_time=task.start_time,
            end_time=task.end_time,
        )

    def create_task(self, task: TaskModel) -> Task:
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return self._to_domain_task(task)

    def get_task_by_tracking_id(self, tracking_id: str) -> Task:
        task_model = (
            self.db.query(TaskModel)
            .filter(TaskModel.tracking_id == tracking_id)
            .first()
        )

        return self._to_domain_task(task_model)

    def update_task(self, task: TaskModel) -> Task:
        self.db.commit()
        self.db.refresh(task)
        return self._to_domain_task(task)

    def delete_task(self, task: TaskModel) -> Task:
        self.db.delete(task)
        self.db.commit()
        return self._to_domain_task(task)
