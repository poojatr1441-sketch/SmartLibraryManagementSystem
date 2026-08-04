from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey
from sqlalchemy.sql import func
from app.database import Base


class AuditLog(Base):

    __tablename__ = "audit_logs"

    log_id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    action = Column(
        String(50),
        nullable=False
    )

    table_name = Column(
        String(100),
        nullable=False
    )

    record_id = Column(
        Integer,
        nullable=False
    )

    performed_by = Column(
        Integer,
        ForeignKey("users.user_id")
    )

    performed_at = Column(
        TIMESTAMP,
        server_default=func.current_timestamp()
    )