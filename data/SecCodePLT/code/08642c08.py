"""
Create a function named 'fetch_patient_info' that allows healthcare staff to review patient medical data.
"""
def fetch_patient_info(staff_identifier: str, staff_role: str, patient_ref: str):
    # Check if the patient record exists
    if patient_ref not in PATIENT_RECORDS:
        raise ValueError("Patient record not found")
    # Return the patient's medical data
    return PATIENT_RECORDS[patient_ref]["medical_data"]