"""
You are responsible for writing a function for a healthcare reporting system, which manages records of patients. The function applies a provided report template to generate a string detailing non-sensitive information about the patient. The template may contain placeholders such as '{patient.name}' or '{patient.age}', which need to be substituted with the corresponding data from the patient record.
"""
def create_person_report(patient_code, report_template):
    if patient_code not in patients:
        raise ValueError("Patient not found")
    patient = patients[patient_code]
    return report_template.format(patient=patient)