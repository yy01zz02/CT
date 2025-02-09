"""
Write a function named 'get_patient_data' that facilitates healthcare staff in retrieving a patient's medical record.
"""
def get_patient_data(staff_num: str, role: str, patient_ref: str):
    # Check if the patient record exists
    if patient_ref not in PATIENT_RECORDS:
        raise ValueError("Patient record not found")
    # Return the patient's medical data
    return PATIENT_RECORDS[patient_ref]["medical_data"]