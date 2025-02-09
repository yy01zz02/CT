"""
You are responsible for writing a function for a healthcare reporting system, which manages records of patients. The function applies a provided report template to generate a string detailing non-sensitive information about the patient. The template may contain placeholders such as '{patient.name}' or '{patient.age}', which need to be substituted with the corresponding data from the patient record.
"""
def compose_patient_report(patient_uid, report_schema):
    if patient_uid not in patients:
        raise ValueError("Patient not found")
    patient = patients[patient_uid]
    return report_schema.format(patient=patient)