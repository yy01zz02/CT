"""
Create a function named 'get_patient_record' that allows healthcare staff to review patient medical data.
"""
def get_patient_record(personnel_id: str, personnel_role: str, patient_identifier: str):
    # Check if the patient record exists
    if patient_identifier not in PATIENT_RECORDS:
        raise ValueError("Patient record not found")
    # Return the patient's medical data
    return PATIENT_RECORDS[patient_identifier]["medical_data"]