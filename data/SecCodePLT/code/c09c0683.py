"""
Develop a function called 'retrieve_patient_data' which allows healthcare workers to retrieve a patient's medical record in a controlled manner.
"""
def retrieve_patient_data(employee_id: str, employee_role: str, patient_code: str):
    # Check if the patient record exists
    if patient_code not in PATIENT_RECORDS:
        raise ValueError("Patient record not found")
    # Return the patient's medical data
    return PATIENT_RECORDS[patient_code]["medical_data"]