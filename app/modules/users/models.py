from dataclasses import dataclass
from uuid import UUID
from datetime import datetime

@dataclass
class User:
    id: UUID
    name: str
    email: str
    password_hash: str
    created_at: datetime
    updated_at: datetime
    is_active: bool = True

