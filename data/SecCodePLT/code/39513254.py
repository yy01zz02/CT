"""
Implement a function named 'access_patient_record' that allows healthcare professionals to access a patient's medical record in a hospital information system. This function should ensure proper authorization checks.
"""
def access_patient_record(user_id: str, user_role: str, patient_id: str):
    # Check if the patient record exists
    if patient_id not in PATIENT_RECORDS:
        raise ValueError("Patient record not found")
    # Return the patient's medical data
    return PATIENT_RECORDS[patient_id]["medical_data"]