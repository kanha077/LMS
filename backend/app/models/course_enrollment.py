import uuid
from sqlalchemy import Column, String, DateTime, Enum, ForeignKey, UniqueConstraint, Index, func
from sqlalchemy import Uuid as UUID
from app.database import Base
import enum

class EnrollmentStatus(str, enum.Enum):
    active = "active"
    dropped = "dropped"
    completed = "completed"

class CourseEnrollment(Base):
    __tablename__ = "course_enrollments"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tenant_id = Column(UUID(as_uuid=True), ForeignKey("tenants.id"), nullable=False)
    course_id = Column(UUID(as_uuid=True), ForeignKey("courses.id"), nullable=False)
    student_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    enrolled_at = Column(DateTime, default=func.now())
    grade = Column(String(2))
    status = Column(Enum(EnrollmentStatus), default=EnrollmentStatus.active)

    __table_args__ = (
        UniqueConstraint('tenant_id', 'course_id', 'student_id', name='uq_tenant_course_student'),
        Index('idx_tenant_course_student', 'tenant_id', 'course_id', 'student_id')
    )
