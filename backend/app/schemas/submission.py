from pydantic import BaseModel, ConfigDict
from typing import Optional
from uuid import UUID
from datetime import datetime
from app.models.submission import SubmissionStatus

class SubmissionBase(BaseModel):
    submission_text: Optional[str] = None
    submission_file_url: Optional[str] = None

class SubmissionCreate(SubmissionBase):
    pass

class SubmissionGrade(BaseModel):
    grade: int
    grade_comment: Optional[str] = None

class SubmissionResponse(SubmissionBase):
    id: UUID
    tenant_id: UUID
    assignment_id: UUID
    student_id: UUID
    submitted_at: Optional[datetime] = None
    is_late: bool
    grade: Optional[int] = None
    grade_comment: Optional[str] = None
    graded_at: Optional[datetime] = None
    graded_by: Optional[UUID] = None
    status: SubmissionStatus
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
