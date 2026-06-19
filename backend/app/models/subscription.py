import uuid
from sqlalchemy import Column, String, Integer, DateTime, func, Text
from sqlalchemy import Uuid as UUID
from app.database import Base

class SubscriptionTier(Base):
    __tablename__ = "subscription_tiers"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(50), nullable=False) # Free, Pro, Enterprise
    max_users = Column(Integer, default=50)
    max_courses = Column(Integer, default=5)
    max_storage_mb = Column(Integer, default=1024)
    features = Column(Text, nullable=True) # JSON encoded string
    created_at = Column(DateTime, default=func.now())
