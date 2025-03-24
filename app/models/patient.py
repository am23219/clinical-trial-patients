from sqlalchemy import Column, Integer, String, JSON
from app.database import Base

class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False, index=True)
    birth_date = Column(String, nullable=False)  # Store as ISO format string "YYYY-MM-DD"
    diagnosed_conditions = Column(JSON, nullable=False)
    current_medications = Column(JSON, nullable=False)
    zip_code = Column(String, nullable=Fe)
    phone_number = Column(String, nullable=False, index=True)
    
