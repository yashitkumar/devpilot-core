from fastapi import APIRouter, Depends, status

from app.core.dependencies import get_current_user
from app.modules.projects.dependencies import get_project_service
from app.modules.projects.schemas import ProjectCreate, ProjectResponse
from app.modules.projects.service import ProjectService
from app.modules.users.models import User

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
    return project_service.create_project(
        project_data=project_data,
        owner_id=current_user.id,
    )