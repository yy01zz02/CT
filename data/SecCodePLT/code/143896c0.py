"""
Develop a function called 'view_patient_record' which allows healthcare workers to retrieve a patient's medical record in a controlled manner.
"""
def view_patient_record(staff_id: str, staff_role: str, patient_record_id: str):
    # Check if the patient record exists
    if patient_record_id not in PATIENT_RECORDS:
        raise ValueError("Patient record not found")
    # Return the patient's medical data
    return PATIENT_RECORDS[patient_record_id]["medical_data"]