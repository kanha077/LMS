from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from app.database import get_db
from app.models.user import User
from app.models.tenant import Tenant
from app.schemas.user import UserCreate, UserResponse, Token
from app.schemas.common import SuccessResponse
from app.security import verify_password, get_password_hash, create_access_token, create_refresh_token
from uuid import UUID

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/register", response_model=SuccessResponse[UserResponse])
def register(user_data: UserCreate, db: Session = Depends(get_db)):
    # Find existing tenant or create dynamically
    tenant = db.query(Tenant).filter(Tenant.name == user_data.tenant_name).first()
    if not tenant:
        import re
        subdomain = re.sub(r'[^a-z0-9]', '', user_data.tenant_name.lower())
        # Ensure subdomain is unique (naive approach)
        existing_sub = db.query(Tenant).filter(Tenant.subdomain == subdomain).first()
        if existing_sub:
            subdomain = subdomain + str(db.query(Tenant).count())

        tenant = Tenant(name=user_data.tenant_name, subdomain=subdomain)
        db.add(tenant)
        db.commit()
        db.refresh(tenant)

    existing_user = db.query(User).filter(User.email == user_data.email, User.tenant_id == tenant.id).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered in this organization")

    hashed_password = get_password_hash(user_data.password)
    new_user = User(
        tenant_id=tenant.id,
        email=user_data.email,
        password_hash=hashed_password,
        full_name=user_data.full_name,
        role=user_data.role
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return {"success": True, "data": new_user, "message": "User registered successfully"}

@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == form_data.username).first()
    if not user or not verify_password(form_data.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = create_access_token(
        data={"sub": str(user.id), "tenant_id": str(user.tenant_id), "role": user.role.value}
    )
    refresh_token = create_refresh_token(
        data={"sub": str(user.id)}
    )
    return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}
