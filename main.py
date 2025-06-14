students = []

def add_student():
    roll = input("Enter Roll Number: ")

    # Check if roll number already exists
    for student in students:
        if student['roll'] == roll:
            print("❌ Roll number already exists!")
            return

    name = input("Enter Name: ")

    try:
        cgpa = float(input("Enter CGPA (0 - 10): "))
        if cgpa < 0 or cgpa > 10:
            print("❌ CGPA must be between 0 and 10.")
            return
    except ValueError:
        print("❌ Invalid CGPA. Please enter a number.")
        return

    student = {
        "roll": roll,
        "name": name,
        "cgpa": cgpa
    }

    students.append(student)
    print("✅ Student added successfully!")

def show_menu():
    print("\n📚 Student CGPA Ranking System")
    print("1. Add Student")
    print("2. Exit")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1 or 2): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
