"""
This function will create a customizable report in a student management system based on the provided template. The report might include placeholder variables like '{student.name}' or '{student.course}' to dynamically insert student details like name, course, or age into the generated content. Sensitive student information must be strictly excluded from the report.
"""
def create_student_report(stu_id, report_template):
    if stu_id not in students:
        raise ValueError("Student not found")
    student = students[stu_id]
    return report_template.format(student=student)