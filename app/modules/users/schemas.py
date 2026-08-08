from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserCreate(BaseModel):
  email: EmailStr
  name: str = Field(min_length=2)
  password: str = Field(min_length=8)

class UserResponse(BaseModel):
  model_config = ConfigDict(from_attributes=True)
  id: UUID
  name: str
  email: EmailStr
  created_at: datetime
  is_active: bool
  