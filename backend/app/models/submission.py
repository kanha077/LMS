import uuid
from sqlalchemy import Column, String, Text, Integer, Boolean, DateTime, Enum, ForeignKey, UniqueConstraint, Index, func
from sqlalchemy import Uuid as UUID
from app.database import Base
import enum

class SubmissionStatus(str, enum.Enum):
    draft = "draft"
    submitted = "submitted"
    graded = "graded"
    returned = "returned"

class Submission(Base):
    __tablename__ = "submissions"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tenant_id = Column(UUID(as_uuid=True), ForeignKey("tenants.id"), nullable=False)
    assignment_id = Column(UUID(as_uuid=True), ForeignKey("assignments.id"), nullable=False)
    student_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    submission_text = Column(Text)
    submission_file_url = Column(String(500))
    submitted_at = Column(DateTime)
    is_late = Column(Boolean, default=False)
    grade = Column(Integer)
    grade_comment = Column(Text)
    graded_at = Column(DateTime)
    graded_by = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    status = Column(Enum(SubmissionStatus), default=SubmissionStatus.draft)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    __table_args__ = (
        UniqueConstraint('tenant_id', 'assignment_id', 'student_id', name='uq_tenant_assignment_student'),
        Index('idx_tenant_assignment_student', 'tenant_id', 'assignment_id', 'student_id')
    )
