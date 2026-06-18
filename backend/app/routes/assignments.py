from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.assignment import Assignment
from app.models.user import User, UserRole
from app.schemas.assignment import AssignmentCreate, AssignmentResponse
from app.schemas.common import SuccessResponse
from app.middleware.auth import get_current_user
import uuid

router = APIRouter(prefix="/assignments", tags=["Assignments"])

@router.get("/", response_model=SuccessResponse[list[AssignmentResponse]])
def get_assignments(course_id: uuid.UUID = None, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    query = db.query(Assignment).filter(Assignment.tenant_id == current_user.tenant_id)
    if course_id:
        query = query.filter(Assignment.course_id == course_id)
    assignments = query.all()
    return {"success": True, "data": assignments, "message": "Successfully retrieved assignments"}

@router.post("/", response_model=SuccessResponse[AssignmentResponse])
def create_assignment(course_id: uuid.UUID, assignment: AssignmentCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if current_user.role not in [UserRole.admin, UserRole.teacher]:
        raise HTTPException(status_code=403, detail="Not authorized to create assignments")
    
    new_assignment = Assignment(
        tenant_id=current_user.tenant_id,
        course_id=course_id,
        title=assignment.title,
        description=assignment.description,
        instructions=assignment.instructions,
        due_date=assignment.due_date,
        total_points=assignment.total_points,
        created_by=current_user.id,
        is_published=assignment.is_published
    )
    db.add(new_assignment)
    db.commit()
    db.refresh(new_assignment)
    return {"success": True, "data": new_assignment, "message": "Assignment created successfully"}
