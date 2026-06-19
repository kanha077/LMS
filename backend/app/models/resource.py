import uuid
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, func
from sqlalchemy import Uuid as UUID
from app.database import Base

class Resource(Base):
    __tablename__ = "resources"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    course_id = Column(UUID(as_uuid=True), ForeignKey("courses.id"), nullable=True)
    lesson_id = Column(UUID(as_uuid=True), ForeignKey("lessons.id"), nullable=True)
    title = Column(String(255), nullable=False)
    resource_type = Column(String(50), nullable=False) # pdf, video, link, zip
    file_url = Column(String(1024), nullable=False)
    file_size = Column(Integer, nullable=True) # in bytes
    created_at = Column(DateTime, default=func.now())
