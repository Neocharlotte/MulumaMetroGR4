from student_manager import grades

def compute_average(name):
    if name in grades and grades[name]:
        return sum(grades[name]) / len(grades[name])
    return 0

def class_average():
    total = 0
    count = 0
    for scores in grades.values():
        total += sum(scores)
        count += len(scores)
    return total / count if count > 0 else 0

def find_top_performer():
    if not grades:
        print("No students available.")
        return
    top_student = max(grades, key=lambda name: compute_average(name))
    print(f"Top performer: {top_student} with average {compute_average(top_student):.2f}")
