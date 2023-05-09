from datetime import datetime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from .database import Base

class IqmApiLog(Base):
    __tablename__ = "iqm_api_log"
    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String(255))
    value = Column(Integer)
    
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True)
    hashed_password = Column(String(255))
    is_active = Column(Boolean, default=True)

    def __repr__(self):
        return f"{self.email}"