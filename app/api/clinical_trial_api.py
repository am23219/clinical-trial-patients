from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.clinical_trial import ClinicalTrial as ClinicalTrialModel
from app.schemas.clinical_trial_schema import ClinicalTrialCreate, ClinicalTrial
from app.services.clinical_trial_service import ClinicalTrialService
from typing import List

router = APIRouter(prefix="/clinical-trials", tags=["Clinical Trials"])

@router.post("/", response_model=ClinicalTrial)
async def create_clinical_trial(trial: ClinicalTrialCreate, db: Session = Depends(get_db)):
   return clinical_trial_service.create_trial(db, trial)

@router.get("/", response_model=List[ClinicalTrial])
async def get_all_clinical_trials(db: Session = Depends(get_db)):
    return clinical_trial_service.get_all_trials(db)

@router.get("/{trial_id}", response_model=ClinicalTrial)
async def get_clinical_trial(trial_id: int, db: Session = Depends(get_db)):
    return clinical_trial_service.get_trial(db, trial_id)

@router.put("/{trial_id}", response_model=ClinicalTrial)
async def update_clinical_trial(trial_id: int, trial: ClinicalTrialCreate, db: Session = Depends(get_db)):
    return clinical_trial_service.update_trial(db, trial_id, trial)