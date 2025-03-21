# clinical-trial-patients

I asked ChatGPT to write me project instructions for a project that would challenge me in my OOP skills. The following were the instructions it gave me, and the code is my process of learning, testing, and trying.

## Project: Clinical Trial Patient Qualification System

### Overview
You will build an object-oriented system for managing potential patients signing up for clinical trials. The project will be an API-based backend, simulating patient sign-ups, patient data validation, qualification assessments, and basic statistical analysis of patient populations.

### Key Requirements:
- **OOP Fundamentals:**
  - Define clear classes with appropriate inheritance and composition (e.g., Patient, ClinicalTrial, and QualificationEngine).

- **Libraries Required:**
  - **FastAPI** for API endpoints.
  - **Pydantic** for data validation and serialization.
  - **SQLAlchemy** for ORM database interactions.
  - **NumPy** for statistical analysis on patient data.

### Functional Requirements:
1. **Patient Registration:**
   - Create an API endpoint (`POST /patients/`) for registering new patients.
   - Validate input data rigorously using Pydantic models.

2. **Clinical Trial Creation:**
   - Implement API endpoints (`POST /trials/`, `GET /trials/{id}`) for managing clinical trials.
   - Each trial has clearly defined criteria (age range, health conditions, etc.).

3. **Qualification Engine:**
   - Design an OOP-based engine that matches registered patients against available trials.
   - Implement methods to evaluate patient eligibility according to trial criteria.

4. **Statistical Analysis:**
   - Utilize NumPy to perform statistical analyses (mean, median, standard deviation) on patient demographics (age, BMI, etc.).
   - Expose an API endpoint (`GET /statistics/`) that returns summarized statistics for analytical purposes.

### Technical Specifications:
- **Database Models:**
  - Define SQLAlchemy ORM models for persistent storage (Patients, Trials, QualificationResults).

- **Validation & Serialization:**
  - Pydantic models should enforce data integrity for both input validation and output serialization.

- **Code Organization:**
  - Use separate Python modules for Models, Schemas, Services, and APIs for clear separation of concerns and OOP best practices.

### Advanced Challenge (Optional):
- Implement detailed logging with Python’s built-in `logging` module.
- Add asynchronous database operations using `async` capabilities provided by FastAPI and SQLAlchemy.

### Deliverables:
- A fully documented GitHub repository.
- Unit tests demonstrating functionality and covering edge cases.
- A brief report (README) summarizing the architecture, OOP principles used, challenges encountered, and lessons learned.

