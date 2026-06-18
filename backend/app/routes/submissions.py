from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.submission import Submission, SubmissionStatus
from app.models.assignment import Assignment
from app.models.user import User, UserRole
from app.schemas.submission import SubmissionCreate, SubmissionResponse, SubmissionGrade
from app.schemas.common import SuccessResponse
from app.middleware.auth import get_current_user
import uuid
from datetime import datetime

router = APIRouter(prefix="/submissions", tags=["Submissions"])

@router.get("/", response_model=SuccessResponse[list[SubmissionResponse]])
def get_submissions(assignment_id: uuid.UUID = None, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    query = db.query(Submission).filter(Submission.tenant_id == current_user.tenant_id)
    if assignment_id:
        query = query.filter(Submission.assignment_id == assignment_id)
    if current_user.role == UserRole.student:
        query = query.filter(Submission.student_id == current_user.id)
    submissions = query.all()
    return {"success": True, "data": submissions, "message": "Successfully retrieved submissions"}

@router.post("/{assignment_id}", response_model=SuccessResponse[SubmissionResponse])
def create_submission(assignment_id: uuid.UUID, submission: SubmissionCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if current_user.role != UserRole.student:
        raise HTTPException(status_code=403, detail="Only students can submit assignments")
        
    assignment = db.query(Assignment).filter(Assignment.id == assignment_id, Assignment.tenant_id == current_user.tenant_id).first()
    if not assignment:
        raise HTTPException(status_code=404, detail="Assignment not found")

    new_submission = Submission(
        tenant_id=current_user.tenant_id,
        assignment_id=assignment_id,
        student_id=current_user.id,
        submission_text=submission.submission_text,
        submission_file_url=submission.submission_file_url,
        submitted_at=datetime.utcnow(),
        is_late=datetime.utcnow() > assignment.due_date,
        status=SubmissionStatus.submitted
    )
    db.add(new_submission)
    db.commit()
    db.refresh(new_submission)
    return {"success": True, "data": new_submission, "message": "Submission created successfully"}
