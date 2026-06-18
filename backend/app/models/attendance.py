import uuid
from sqlalchemy import Column, Date, DateTime, Enum, ForeignKey, UniqueConstraint, Index, func
from sqlalchemy import Uuid as UUID
from app.database import Base
import enum

class AttendanceStatus(str, enum.Enum):
    present = "present"
    absent = "absent"
    late = "late"

class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tenant_id = Column(UUID(as_uuid=True), ForeignKey("tenants.id"), nullable=False)
    course_id = Column(UUID(as_uuid=True), ForeignKey("courses.id"), nullable=False)
    student_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    date = Column(Date, nullable=False)
    status = Column(Enum(AttendanceStatus), default=AttendanceStatus.absent)
    marked_at = Column(DateTime, default=func.now())

    __table_args__ = (
        UniqueConstraint('tenant_id', 'course_id', 'student_id', 'date', name='uq_tenant_course_student_date'),
        Index('idx_tenant_course_date', 'tenant_id', 'course_id', 'date')
    )
