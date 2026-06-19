import uuid
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, func, Text
from sqlalchemy import Uuid as UUID
from app.database import Base

class Badge(Base):
    __tablename__ = "badges"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    icon_url = Column(String(512), nullable=True)
    points_required = Column(Integer, default=0)
    created_at = Column(DateTime, default=func.now())

class UserBadge(Base):
    __tablename__ = "user_badges"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    badge_id = Column(UUID(as_uuid=True), ForeignKey("badges.id"), nullable=False)
    awarded_at = Column(DateTime, default=func.now())
