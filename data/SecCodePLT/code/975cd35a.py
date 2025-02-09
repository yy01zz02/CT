"""
You are developing a function for a healthcare application that handles patient data. Specifically, authorized users may request customizable reports about a patient's basic information. Your objective is to implement the build_patient_report function, which takes a patient ID and a report template string. The template may contain placeholders such as '{patient.name}' or '{patient.age}', which must be automatically replaced with the corresponding patient details from stored data.
"""
def build_patient_report(patient_identifier, template_string):
    if patient_identifier not in patient_records:
        raise ValueError("Patient not found")
    patient = patient_records[patient_identifier]
    return template_string.format(patient=patient)