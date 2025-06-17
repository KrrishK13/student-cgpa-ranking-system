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

def selection_sort():
    n = len(students)
    for i in range(n):
        max_idx = i
        for j in range(i + 1, n):
            if students[j]['cgpa'] > students[max_idx]['cgpa']:
                max_idx = j
        students[i], students[max_idx] = students[max_idx], students[i]
    print("✅ Students sorted by CGPA using Selection Sort.")

def merge_sort(student_list):
    if len(student_list) <= 1:
        return student_list

    mid = len(student_list) // 2
    left = merge_sort(student_list[:mid])
    right = merge_sort(student_list[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    while left and right:
        if left[0]['cgpa'] > right[0]['cgpa']:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left + right)
    return result

def sort_students():
    if not students:
        print("❌ No student records to sort.")
        return

    print("\nChoose Sorting Method:")
    print("1. Selection Sort")
    print("2. Merge Sort")

    choice = input("Enter choice (1 or 2): ")

    if choice == '1':
        selection_sort()
    elif choice == '2':
        sorted_list = merge_sort(students)
        students.clear()
        students.extend(sorted_list)
        print("✅ Students sorted by CGPA using Merge Sort.")
    else:
        print("❌ Invalid choice.")

def view_students():
    if not students:
        print("❌ No students to display.")
        return

    print("\n📋 List of Students:")
    print("{:<10} {:<20} {:<5}".format("Roll", "Name", "CGPA"))
    print("-" * 40)
    for s in students:
        print("{:<10} {:<20} {:<5}".format(s['roll'], s['name'], s['cgpa']))

def sort_students():
    if not students:
        print("❌ No student records to sort.")
        return

    print("\nChoose Sorting Method:")
    print("1. Selection Sort")
    print("2. Merge Sort")

    choice = input("Enter choice (1 or 2): ")

    if choice == '1':
        selection_sort()
        view_students()  # 👈 Show sorted list
    elif choice == '2':
        sorted_list = merge_sort(students)
        students.clear()
        students.extend(sorted_list)
        print("✅ Students sorted by CGPA using Merge Sort.")
        view_students()  # 👈 Show sorted list
    else:
        print("❌ Invalid choice.")

def show_menu():
    print("\n📚 Student CGPA Ranking System")
    print("1. Add Student")
    print("2. Update Student")
    print("3. Delete Student")
    print("4. Sort Students by CGPA")
    print("5. View All Students")
    print("5. Exit")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1–5): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            update_student()
        elif choice == '3':
            delete_student()
        elif choice == '4':
            sort_students()
        elif choice == '5':
            view_students()
        elif choice == '6':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
