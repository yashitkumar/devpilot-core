from uuid import UUID
from app.modules.projects.repository import ProjectRepository
from app.modules.tasks.models import Task
from app.modules.tasks.repository import TaskRepository
from app.modules.tasks.schemas import TaskCreate

class TaskService:
    def __init__(self, task_repository: TaskRepository, project_repository: ProjectRepository):
        self._task_repository = task_repository
        self._project_repository = project_repository

    def create_task(
        self,
        project_id: UUID,
        task_data: TaskCreate,
        owner_id: UUID,
    ) -> Task:
        project = self._project_repository.get_by_id(project_id)

        if project is None:
            raise ValueError("Project not found")

        if project.owner_id != owner_id:
            raise PermissionError(
                "You do not have access to this project"
            )

        task = Task(
            title=task_data.title,
            description=task_data.description,
            project_id=project_id,
        )

        return self._task_repository.create(task)

    def get_tasks(
        self,
        project_id: UUID,
        owner_id: UUID,
    ) -> list[Task]:
        project = self._project_repository.get_by_id(project_id)

        if project is None:
            raise ValueError("Project not found")

        if project.owner_id != owner_id:
            raise PermissionError(
                "You do not have access to this project"
            )

        return self._task_repository.get_by_project(project_id)

    def get_task(
        self,
        task_id: UUID,
        owner_id: UUID,
    ) -> Task:
        task = self._task_repository.get_by_id(task_id)

        if task is None:
            raise ValueError("Task not found")

        project = self._project_repository.get_by_id(task.project_id)

        if project is None:
            raise ValueError("Project not found")

        if project.owner_id != owner_id:
            raise PermissionError(
                "You do not have access to this task"
            )

        return task

    def delete_task(
        self,
        task_id: UUID,
        owner_id: UUID,
    ) -> None:
        task = self._task_repository.get_by_id(task_id)

        if task is None:
            raise ValueError("Task not found")

        project = self._project_repository.get_by_id(task.project_id)

        if project is None:
            raise ValueError("Project not found")

        if project.owner_id != owner_id:
            raise PermissionError(
                "You do not have access to this task"
            )

        self._task_repository.delete(task)