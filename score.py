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


students = {}

while True:
    print("\n===== Student Score Tracker =====")
    print("1. Add student")
    print("2. View students")
    print("3. Search student")
    print("4. Calculate average")
    print("5. Highest score")
    print("6. Lowest score")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        name = input("Enter student name: ")
        score = float(input("Enter student score: "))

        students[name] = score
        print("Student added successfully.")

    elif choice == "2":
        if not students:
            print("No students found.")
        else:
            for name, score in students.items():
                print(f"{name}: {score}")

    elif choice == "3":
        name = input("Enter student name to search: ")

        if name in students:
            print(f"{name}: {students[name]}")
        else:
            print("Student not found.")

    elif choice == "4":
        if not students:
            print("No scores available.")
        else:
            average = sum(students.values()) / len(students)
            print(f"Average score: {average:.2f}")

    elif choice == "5":
        if not students:
            print("No scores available.")
        else:
            highest = max(students, key=students.get)
            print(f"Highest score: {highest} - {students[highest]}")

    elif choice == "6":
        if not students:
            print("No scores available.")
        else:
            lowest = min(students, key=students.get)
            print(f"Lowest score: {lowest} - {students[lowest]}")

    elif choice == "7":
        print("Thank you for using Student Score Tracker.")
        break

    else:
        print("Invalid choice. Please try again.")