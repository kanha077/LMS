from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.course import Course
from app.models.user import User, UserRole
from app.schemas.course import CourseCreate, CourseResponse
from app.schemas.common import SuccessResponse
from app.middleware.auth import get_current_user

router = APIRouter(prefix="/courses", tags=["Courses"])

@router.get("/", response_model=SuccessResponse[list[CourseResponse]])
def get_courses(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    courses = db.query(Course).filter(Course.tenant_id == current_user.tenant_id).all()
    return {"success": True, "data": courses, "message": "Successfully retrieved courses"}

@router.post("/", response_model=SuccessResponse[CourseResponse])
def create_course(course: CourseCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if current_user.role not in [UserRole.admin, UserRole.teacher]:
        raise HTTPException(status_code=403, detail="Not authorized to create courses")
    
    new_course = Course(
        tenant_id=current_user.tenant_id,
        name=course.name,
        description=course.description,
        code=course.code,
        teacher_id=current_user.id,
        semester=course.semester
    )
    db.add(new_course)
    db.commit()
    db.refresh(new_course)
    return {"success": True, "data": new_course, "message": "Course created successfully"}
