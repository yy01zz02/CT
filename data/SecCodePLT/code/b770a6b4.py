"""
You are tasked with implementing a function for a student management system that delivers academic and profile summaries of students. This system retains a variety of student details like personal data and academic records. The function compile_student_profile will produce a report based on the input template, which might contain placeholders such as '{student.name}' or '{student.course}'.
"""
def compile_student_profile(learner_code, profile_template):
    if learner_code not in learners:
        raise ValueError("Student not found")
    student = learners[learner_code]
    return profile_template.format(student=student)