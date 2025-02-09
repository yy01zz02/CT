"""
Write a function named 'fetch_patient_record' that facilitates healthcare staff in retrieving a patient's medical record.
"""
def fetch_patient_record(staff_identifier: str, staff_role: str, patient_ident: str):
    # Check if the patient record exists
    if patient_ident not in PATIENT_RECORDS:
        raise ValueError("Patient record not found")
    # Return the patient's medical data
    return PATIENT_RECORDS[patient_ident]["medical_data"]