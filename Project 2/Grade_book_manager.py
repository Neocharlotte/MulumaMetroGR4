#NEO

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

#NSUKU

# grade_display.py


# Example student grades data
grades = {
    "Neo": [80, 90, 85],
    "Nsuku": [70, 75, 80],
    "Lavani": [95, 100, 90]
}

# Function to compute the average for a single student
def compute_average(name):
    scores = grades[name]
    return sum(scores) / len(scores)

# Function to compute the average for the whole class
def class_average():
    total = 0
    count = 0
    for scores in grades.values():
        total += sum(scores)
        count += len(scores)
    return total / count

# Function to display all averages
def display_averages():
    if not grades:
        print("No student records found.")
        return

    print("\nStudent Averages:")
    for name in grades:
        avg = compute_average(name)
        print(f"{name}: {avg:.2f}")
    print(f"\nClass Average: {class_average():.2f}")

# Run the function to show results
display_averages()
