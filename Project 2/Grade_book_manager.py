grades = {} 

#Lavani: Student Management
def add_student(name):
    if name in grades:
        print(f"{name} is already in the gradebook.")
    else:
        grades[name] = []
        print(f"{name} has been added to the gradebook.")

def record_grade(name, score):
    if name not in grades:
        print(f"{name} is not in the gradebook. Please add them first.")
    else:
        grades[name].append(score)
        print(f"Recorded score {score} for {name}.")

# Neo: Average and Top Performer 
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

#Nsuku: Display Averages 
def display_averages():
    if not grades:
        print("No student records found.")
        return

    print("\nStudent Averages:")
    for name in grades:
        avg = compute_average(name)
        print(f"{name}: {avg:.2f}")
    print(f"\nClass Average: {class_average():.2f}")

# N_M: User Interface 
def main_menu():
    while True:
        print("\nGradebook Menu:")
        print("1. Add student")
        print("2. Add grade")
        print("3. View student average")
        print("4. View class report")
        print("5. Exit")

        choice = input("Enter your choice (1–5): ")

        if choice == '1':
            name = input("Enter student name to add: ")
            add_student(name)
        elif choice == '2':
            name = input("Enter student name: ")
            try:
                score = float(input("Enter grade to record: "))
                record_grade(name, score)
            except ValueError:
                print("Invalid grade. Please enter a number.")
        elif choice == '3':
            name = input("Enter student name to view average: ")
            if name in grades:
                avg = compute_average(name)
                print(f"{name}'s average: {avg:.2f}")
            else:
                print(f"{name} is not in the gradebook.")
        elif choice == '4':
            display_averages()
            find_top_performer()
        elif choice == '5':
            print("Exiting Gradebook. Goodbye!")
            break
        else:
            print("Invalid choice. Please select from 1 to 5.")

#  Run Menu 
if __name__ == "__main__":
    main_menu()
