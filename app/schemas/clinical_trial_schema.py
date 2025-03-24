from pydantic import BaseModel, Field
from datetime import date
from typing import List, Optional   


class ClinicalTrialCreate(BaseModel):
    id: int = Field(..., default=None, primary_key=True)
    title: str = Field(..., min_length=1, max_length=200, example="Diabetes Type 2 Treatment Study")
    description: str = Field(..., min_length=10, example="A study to evaluate the efficacy of a new medication for Type 2 Diabetes")
    status: str = Field(..., description="Current status of the trial. Choose from: 'Recruiting', 'Enrolling', 'Completed'", example="Recruiting")
    min_age: int = Field(..., ge=0, le=120, example=18)
    max_age: int = Field(..., ge=0, le=120, example=65)
    required_conditions: List[str] = Field(..., example=["Diabetes Type 2"])
    
class ClinicalTrial(ClinicalTrialCreate):
    id: int
    
    class Config:
        orm_mode = True
        
        
