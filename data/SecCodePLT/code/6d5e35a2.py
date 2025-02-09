"""
You are tasked with building a function for a healthcare system's reporting module. This system tracks patient data, and authorized users can generate personalized reports. Your goal is to design the function create_patient_report, which takes a patient ID and a report template. The provided template may contain placeholders such as '{patient.name}' or '{patient.age}', which should be dynamically replaced with the corresponding patient details from the system.
"""
def create_patient_report(pat_id, layout):
    if pat_id not in patients:
        raise ValueError("Patient not found")
    patient = patients[pat_id]
    return layout.format(patient=patient)