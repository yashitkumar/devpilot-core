from uuid import UUID

from app.modules.projects.models import Project
from app.modules.projects.repository import ProjectRepository
from app.modules.projects.schemas import ProjectCreate


class ProjectService:

    def __init__(self, repository: ProjectRepository):
        self._repository = repository

    def create_project(
        self,
        project_data: ProjectCreate,
        owner_id: UUID,
    ) -> Project:
        project = Project(
            name=project_data.name,
            description=project_data.description,
            owner_id=owner_id,
        )

        return self._repository.create(project)

    def get_project(
        self,
        project_id: UUID,
        owner_id: UUID,
    ) -> Project:
        project = self._repository.get_by_id(project_id)

        if project is None:
            raise ValueError("Project not found")

        if project.owner_id != owner_id:
            raise PermissionError("You do not have access to this project")

        return project

    def get_projects(
        self,
        owner_id: UUID,
    ) -> list[Project]:
        return self._repository.get_by_owner(owner_id)

    def delete_project(
        self,
        project_id: UUID,
        owner_id: UUID,
    ) -> None:
        project = self._repository.get_by_id(project_id)

        if project is None:
            raise ValueError("Project not found")

        if project.owner_id != owner_id:
            raise PermissionError("You do not have access to this project")

        self._repository.delete(project)