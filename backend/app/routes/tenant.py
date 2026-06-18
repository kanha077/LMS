from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.tenant import Tenant
from app.models.user import User, UserRole
from app.schemas.tenant import TenantResponse
from app.schemas.common import SuccessResponse
from app.middleware.auth import get_current_user
import uuid

router = APIRouter(prefix="/tenant", tags=["Tenant Settings"])

@router.get("/settings", response_model=SuccessResponse[TenantResponse])
def get_tenant_settings(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if current_user.role != UserRole.admin:
        raise HTTPException(status_code=403, detail="Not authorized to view tenant settings")
    tenant = db.query(Tenant).filter(Tenant.id == current_user.tenant_id).first()
    return {"success": True, "data": tenant, "message": "Successfully retrieved tenant settings"}
