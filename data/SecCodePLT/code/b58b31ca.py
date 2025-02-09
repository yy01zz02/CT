"""
Develop a function called 'get_patient_data' which allows healthcare workers to retrieve a patient's medical record in a controlled manner.
"""
def get_patient_data(worker_id: str, worker_role: str, record_id: str):
    # Check if the patient record exists
    if record_id not in PATIENT_RECORDS:
        raise ValueError("Patient record not found")
    # Return the patient's medical data
    return PATIENT_RECORDS[record_id]["medical_data"]