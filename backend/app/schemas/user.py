from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional
from uuid import UUID
from datetime import datetime
from app.models.user import UserRole

class UserBase(BaseModel):
    email: str
    full_name: Optional[str] = None
    role: UserRole = UserRole.student

class UserCreate(UserBase):
    password: str
    tenant_name: str

class UserResponse(UserBase):
    id: UUID
    tenant_id: UUID
    is_active: bool
    email_verified: bool
    created_at: datetime
    updated_at: datetime
    
    model_config = ConfigDict(from_attributes=True)

class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"

class TokenData(BaseModel):
    sub: Optional[str] = None
    tenant_id: Optional[str] = None
    email: Optional[str] = None
    role: Optional[str] = None
