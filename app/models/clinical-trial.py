from sqlalchemy import Column, Integer, String, Boolean, JSON
from app.database import Base
from datetime import date
class ClinicalTrial(Base):
    __tablename__ = "clinical_trials"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullabale=False, unique=True)
    description = Column(String, nullable=False)
    start_date = Column(date, nullable=False)
    end_date = Column(date, nullable=False)
    status = Column(String, nullable=False)

    # Trial criteria
    min_age = Column(Integer, nullable=False)
    max_age = Column(Integer, nullable=False)
    required_conditions = Column(JSON, nullable=False)
    excluded_conditions = Column(JSON, nullable=False)
    excluded_medications = Column(JSON, nullable=False)
    