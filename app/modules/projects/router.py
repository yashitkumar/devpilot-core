from fastapi import APIRouter, Depends, status

from app.core.dependencies import get_current_user
from app.modules.projects.dependencies import get_project_service
from app.modules.projects.schemas import ProjectCreate, ProjectResponse
from app.modules.projects.service import ProjectService
from app.modules.users.models import User
from uuid import UUID

router = APIRouter(
    prefix="/projects",
    tags=["Projects"],
)

@router.post("",response_model=ProjectResponse,status_code=status.HTTP_201_CREATED)

def create_project(
    project_data: ProjectCreate,
    current_user: User = Depends(get_current_user),
    project_service: ProjectService = Depends(get_project_service),
):
    return project_service.create_project(project_data=project_data, owner_id=current_user.id)

@router.get("", response_model=list[ProjectResponse])

def get_projects(
    current_user: User = Depends(get_current_user),
    project_service: ProjectService = Depends(get_project_service),
):
    return project_service.get_projects(
        owner_id=current_user.id,
    )

@router.get("/{project_id}", response_model=ProjectResponse)
def get_project(
    project_id: UUID,
    current_user: User = Depends(get_current_user),
    project_service: ProjectService = Depends(get_project_service),
):
    return project_service.get_project(
        project_id=project_id,
        owner_id=current_user.id,
    )

@router.delete("/{project_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_project(
    project_id: UUID,
    current_user: User = Depends(get_current_user),
    project_service: ProjectService = Depends(get_project_service),
):
    project_service.delete_project(
        project_id=project_id,
        owner_id=current_user.id,
    )    
    
    