from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional
from uuid import UUID
from datetime import datetime

class TenantBase(BaseModel):
    name: str
    subdomain: str
    email: Optional[EmailStr] = None
    subscription_plan: str = "free"

class TenantCreate(TenantBase):
    pass

class TenantResponse(TenantBase):
    id: UUID
    is_active: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
