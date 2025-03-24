from pydantic import BaseModel, Field
from datetime import date
from typing import List, Optional

class PatientCreate(BaseModel):
    id: int = Field(default=None, primary_key=True)
    name: str = Field(..., min_length=1, max_length=100, example="John Doe")
    email: str = Field(..., format="email", example="john.doe@example.com")
    birth_date: date = Field(..., description="Date of birth in YYYY-MM-DD format", example="1990-01-01")
    diagnosed_conditions: List[str] = Field(..., example=["Diabetes", "Hypertension"])
    current_medications: List[str] = Field(..., example=["Aspirin", "Lisinopril"])
    zip_code: str = Field(..., example="12345")
    phone_number: str = Field(..., description="Phone number with country code", example="+1234567890")
    
class Patient(PatientCreate):
    id: int
    
    class Config:
        orm_mode = True
        