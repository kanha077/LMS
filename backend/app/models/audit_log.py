import uuid
from sqlalchemy import Column, String, Text, DateTime, ForeignKey, Index, func
from sqlalchemy import Uuid as UUID
from app.database import Base

class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tenant_id = Column(UUID(as_uuid=True), ForeignKey("tenants.id"), nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    action = Column(String(100), nullable=False)
    resource_type = Column(String(100))
    resource_id = Column(String(100))
    changes = Column(Text)
    ip_address = Column(String(50))
    user_agent = Column(Text)
    created_at = Column(DateTime, default=func.now())

    __table_args__ = (
        Index('idx_tenant_timestamp', 'tenant_id', 'created_at'),
    )
