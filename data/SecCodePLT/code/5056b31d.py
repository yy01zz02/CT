"""
You are developing a function for an educational platform's student management system. The system stores student academic information such as grades and personal details. Your task is to implement the generate_student_report function that creates a report string based on student data. The report should be customizable using a template that may contain fields like '{student.name}' or '{student.course}'.
"""
def generate_student_report(student_id, template):
    if student_id not in students:
        raise ValueError("Student not found")
    student = students[student_id]
    return template.format(student=student)