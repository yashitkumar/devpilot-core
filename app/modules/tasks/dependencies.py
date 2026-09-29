from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.modules.projects.repository import ProjectRepository
from app.modules.tasks.repository import TaskRepository
from app.modules.tasks.service import TaskService


def get_task_repository(
    db: Session = Depends(get_db),
) -> TaskRepository:
    return TaskRepository(db)


def get_project_repository(
    db: Session = Depends(get_db),
) -> ProjectRepository:
    return ProjectRepository(db)


def get_task_service(
    task_repository: TaskRepository = Depends(get_task_repository),
    project_repository: ProjectRepository = Depends(get_project_repository),
) -> TaskService:
    return TaskService(
        task_repository=task_repository,
        project_repository=project_repository,
    )