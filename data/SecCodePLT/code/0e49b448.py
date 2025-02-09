"""
You are responsible for writing a function for a healthcare reporting system, which manages records of patients. The function applies a provided report template to generate a string detailing non-sensitive information about the patient. The template may contain placeholders such as '{patient.name}' or '{patient.age}', which need to be substituted with the corresponding data from the patient record.
"""
def build_patient_summary(patient_key, template_string):
    if patient_key not in patients:
        raise ValueError("Patient not found")
    patient = patients[patient_key]
    return template_string.format(patient=patient)