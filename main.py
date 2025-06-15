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

def update_student():
    roll = input("Enter Roll Number of the student to update: ")
    
    for student in students:
        if student['roll'] == roll:
            print(f"Current Name: {student['name']}")
            print(f"Current CGPA: {student['cgpa']}")
            student['name'] = input("Enter New Name: ")
            
            try:
                cgpa = float(input("Enter New CGPA (0 - 10): "))
                if 0 <= cgpa <= 10:
                    student['cgpa'] = cgpa
                    print("✅ Student updated successfully!")
                else:
                    print("❌ CGPA must be between 0 and 10.")
            except ValueError:
                print("❌ Invalid CGPA input.")
            return

    print("❌ Student with that Roll Number not found.")

def delete_student():
    roll = input("Enter Roll Number of the student to delete: ")
    
    for student in students:
        if student['roll'] == roll:
            students.remove(student)
            print("✅ Student deleted successfully!")
            return

    print("❌ Student with that Roll Number not found.")



def show_menu():
    print("\n📚 Student CGPA Ranking System")
    print("1. Add Student")
    print("2. Update Student")
    print("3. Delete Student")
    print("4. Exit")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1–4): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            update_student()
        elif choice == '3':
            delete_student()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
