"""
This function is meant for generating a student report within an academic management system. Information such as the student’s name, course, and age will be presented in a customizable report format. The provided template can include placeholders like '{student.name}' or '{student.course}' and must not include sensitive data.
"""
def produce_student_report(stu_id, custom_template):
    if stu_id not in students:
        raise ValueError("Student not found")
    student = students[stu_id]
    return custom_template.format(student=student)