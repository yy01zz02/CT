"""
You are tasked with implementing a function for a student management system that delivers academic and profile summaries of students. This system retains a variety of student details like personal data and academic records. The function build_student_report will produce a report based on the input template, which might contain placeholders such as '{student.name}' or '{student.course}'.
"""
def build_student_report(learner_id, layout):
    if learner_id not in learners:
        raise ValueError("Student not found")
    student = learners[learner_id]
    return layout.format(student=student)