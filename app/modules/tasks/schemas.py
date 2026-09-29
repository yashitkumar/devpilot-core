from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, ConfigDict, Field

class TaskCreate(BaseModel):
    title: str = Field(min_length=3, max_length=100)
    description: str = Field(min_length=4, max_length=255)

class TaskResponse(BaseModel):
    id: UUID
    title: str
    description: str
    project_id: UUID
    status: str
    priority: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)