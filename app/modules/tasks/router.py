from uuid import UUID
from fastapi import APIRouter, Depends, status
from app.core.dependencies import get_current_user
from app.modules.tasks.dependencies import get_task_service
from app.modules.tasks.schemas import TaskCreate, TaskResponse
from app.modules.tasks.service import TaskService
from app.modules.users.models import User

router = APIRouter(
    prefix="/projects/{project_id}/tasks",
    tags=["Tasks"],
)

@router.post("", response_model=TaskResponse,status_code=status.HTTP_201_CREATED)
def create_task(
    project_id: UUID,
    task_data: TaskCreate,
    current_user: User = Depends(get_current_user),
    task_service: TaskService = Depends(get_task_service),
):
    return task_service.create_task(
        project_id=project_id,
        task_data=task_data,
        owner_id=current_user.id,
    )

@router.get("",response_model=list[TaskResponse])
def get_tasks(
    project_id: UUID,
    current_user: User = Depends(get_current_user),
    task_service: TaskService = Depends(get_task_service),
):
    return task_service.get_tasks(
        project_id=project_id,
        owner_id=current_user.id,
    )

@router.get("/{task_id}", response_model=TaskResponse)
def get_task(
    project_id: UUID,
    task_id: UUID,
    current_user: User = Depends(get_current_user),
    task_service: TaskService = Depends(get_task_service),
):
    return task_service.get_task(
        task_id=task_id,
        owner_id=current_user.id,
    )

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(
    project_id: UUID,
    task_id: UUID,
    current_user: User = Depends(get_current_user),
    task_service: TaskService = Depends(get_task_service),
):
    task_service.delete_task(
        task_id=task_id,
        owner_id=current_user.id,
    )            