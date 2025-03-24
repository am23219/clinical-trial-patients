from sqlalchemy.orm import Session
from app.models.clinical_trial import ClinicalTrial as ClinicalTrialModel
from app.schemas.clinical_trial_schema import ClinicalTrialCreate, ClinicalTrial

def create_trial(trial: ClinicalTrialCreate, db: Session):
    db_trial = ClinicalTrialModel(**trial.dict())
    db.add(db_trial)
    db.commit()
    db.refresh(db_trial)
    return db_trial
    
def get_all_trials(db: Session):
    return db.query(ClinicalTrialModel).all()

def get_trial(trial_id: int, db: Session):
    return db.query(ClinicalTrialModel).filter(ClinicalTrialModel.id == trial_id).first()

def update_trial(trial_id: int, trial: ClinicalTrialCreate, db: Session):
    db_trial = db.query(ClinicalTrialModel).filter(ClinicalTrialModel.id == trial_id).first()
    if not db_trial:
        raise HTTPException(status_code=404, detail="Trial not found")
    for field, value in trial.dict().items():
        setattr(db_trial, field, value)
        