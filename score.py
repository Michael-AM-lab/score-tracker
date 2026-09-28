students = []

# Functions
def add_student():
    name = input("Enter student name: ")
    score = float(input("Enter student score: "))

    student = {
        "name": name,
        "score": score
    }

    students.append(student)
    print("Student added successfully!")


def view_students():
    if len(students) == 0:
        print("No students found.")
    else:
        print("\nStudent Records")
        for student in students:
            print(f"Name: {student['name']} | Score: {student['score']}")


def search_student():
    name = input("Enter student name to search: ")

    found = False

    for student in students:
        if student["name"].lower() == name.lower():
            print("\nStudent Found")
            print(f"Name: {student['name']}")
            print(f"Score: {student['score']}")
            found = True
            break

    if not found:
        print("Student not registered.")

def calculate_average():
    if len([student["score"] for student in students]) == 0:
        print("No scores available.\n")
    else:
        average = sum([student["score"] for student in students]) / len([student["score"] for student in students])
        print(f"Average Score = {average:.2f}\n")


def highest_score():
    if len([student["score"] for student in students]) == 0:
        print("No scores available.\n")
    else:
        highest = max([student["score"] for student in students])
        index = [student["score"] for student in students].index(highest)
        print(f"Highest Score")
        print(f"Student: {students[index]}")
        print(f"Score: {highest}\n")

def lowest_score():
    if len([student["score"] for student in students]) == 0:
        print("No scores available.\n")
    else:
        lowest = min([student["score"] for student in students])
        index = [student["score"] for student in students].index(lowest)
        print(f"Lowest Score")
        print(f"Student: {students[index]}")
        print(f"Score: {lowest}\n")



