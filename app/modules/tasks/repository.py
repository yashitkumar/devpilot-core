from uuid import UUID
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.modules.tasks.models import Task


class TaskRepository:

    def __init__(self, db: Session):
        self._db = db

    def create(self, task: Task) -> Task:
        self._db.add(task)
        self._db.commit()
        self._db.refresh(task)

        return task

    def get_by_id(self, task_id: UUID) -> Task | None:
        statement = select(Task).where(Task.id == task_id)

        return self._db.scalar(statement)

    def get_by_project(self, project_id: UUID) -> list[Task]:
        statement = (
            select(Task)
            .where(Task.project_id == project_id)
            .order_by(Task.created_at.desc())
        )

        return list(self._db.scalars(statement).all())

    def delete(self, task: Task) -> None:
        self._db.delete(task)
        self._db.commit()