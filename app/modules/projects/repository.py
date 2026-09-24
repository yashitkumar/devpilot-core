from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.modules.projects.models import Project


class ProjectRepository:

    def __init__(self, db: Session):
        self._db = db

    def create(self, project: Project) -> Project:
        self._db.add(project)
        self._db.commit()
        self._db.refresh(project)

        return project

    def get_by_id(self, project_id: UUID) -> Project | None:
        statement = select(Project).where(Project.id == project_id)

        return self._db.scalar(statement)

    def get_by_owner(self, owner_id: UUID) -> list[Project]:
        statement = (
            select(Project)
            .where(Project.owner_id == owner_id)
            .order_by(Project.created_at.desc())
        )

        return list(self._db.scalars(statement).all())

    def delete(self, project: Project) -> None:
        self._db.delete(project)
        self._db.commit()