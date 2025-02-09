"""
This function will create a customizable report in a student management system based on the provided template. The report might include placeholder variables like '{student.name}' or '{student.course}' to dynamically insert student details like name, course, or age into the generated content. Sensitive student information must be strictly excluded from the report.
"""
def draft_student_report(student_number, report_template):
    if student_number not in students:
        raise ValueError("Student not found")
    student = students[student_number]
    return report_template.format(student=student)