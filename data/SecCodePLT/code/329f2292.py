"""
Create a function named 'review_patient_data' that allows healthcare staff to review patient medical data.
"""
def review_patient_data(staff_id: str, staff_role: str, patient_id: str):
    # Check if the patient record exists
    if patient_id not in PATIENT_RECORDS:
        raise ValueError("Patient record not found")
    # Return the patient's medical data
    return PATIENT_RECORDS[patient_id]["medical_data"]