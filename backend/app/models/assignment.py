import uuid
from sqlalchemy import Column, String, Text, Integer, Boolean, DateTime, ForeignKey, Index, func
from sqlalchemy import Uuid as UUID
from app.database import Base

class Assignment(Base):
    __tablename__ = "assignments"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tenant_id = Column(UUID(as_uuid=True), ForeignKey("tenants.id"), nullable=False)
    course_id = Column(UUID(as_uuid=True), ForeignKey("courses.id"), nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(Text)
    instructions = Column(Text)
    due_date = Column(DateTime, nullable=False)
    total_points = Column(Integer, default=100)
    created_by = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    is_published = Column(Boolean, default=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    __table_args__ = (
        Index('idx_tenant_course_due', 'tenant_id', 'course_id', 'due_date'),
    )
