"""
You are tasked with implementing a function for a student management system that delivers academic and profile summaries of students. This system retains a variety of student details like personal data and academic records. The function create_student_summary will produce a report based on the input template, which might contain placeholders such as '{student.name}' or '{student.course}'.
"""
def create_student_summary(stu_id, summary_template):
    if stu_id not in students:
        raise ValueError("Student not found")
    student = students[stu_id]
    return summary_template.format(student=student)