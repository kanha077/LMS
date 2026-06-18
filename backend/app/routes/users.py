from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User
from app.schemas.user import UserResponse
from app.schemas.common import SuccessResponse
from app.middleware.auth import get_current_user

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/me", response_model=SuccessResponse[UserResponse])
def get_me(current_user: User = Depends(get_current_user)):
    return {"success": True, "data": current_user, "message": "Successfully retrieved user profile"}

@router.get("/", response_model=SuccessResponse[list[UserResponse]])
def get_users(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    users = db.query(User).filter(User.tenant_id == current_user.tenant_id).all()
    return {"success": True, "data": users, "message": "Successfully retrieved users"}
