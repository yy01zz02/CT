"""
You are developing a function for a healthcare application that handles patient data. Specifically, authorized users may request customizable reports about a patient's basic information. Your objective is to implement the create_patient_report function, which takes a patient ID and a report template string. The template may contain placeholders such as '{patient.name}' or '{patient.age}', which must be automatically replaced with the corresponding patient details from stored data.
"""
def create_patient_report(id, report_template):
    if id not in patients:
        raise ValueError("Patient not found")
    patient = patients[id]
    return report_template.format(patient=patient)