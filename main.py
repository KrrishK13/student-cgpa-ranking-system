students = []

def add_student():
    roll = input("Enter Roll Number: ").strip()

    # Check if roll number already exists
    for student in students:
        if student['roll'] == roll:
            print("❌ Roll number already exists!")
            return

    name = input("Enter Name: ").strip()
    if not name:
        print("❌ Name cannot be empty.")
        return

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
        "cgpa": cgpa,
        "medal": None
    }

    students.append(student)
    print("✅ Student added successfully!")
    print("-" * 50)



def update_student():
    roll = input("Enter Roll Number of the student to update: ").strip()
    if not roll:
        print("❌ Roll Number cannot be empty.")
        return

    for student in students:
        if student['roll'] == roll:
            print(f"Current Name: {student['name']}")
            print(f"Current CGPA: {student['cgpa']}")

            name = input("Enter New Name: ").strip()
            if not name:
                print("❌ Name cannot be empty.")
                return
            student['name'] = name

            try:
                cgpa = float(input("Enter New CGPA (0 - 10): "))
                if 0 <= cgpa <= 10:
                    student['cgpa'] = cgpa
                    print("✅ Student updated successfully!")
                    print("-" * 50)

                else:
                    print("❌ CGPA must be between 0 and 10.")
            except ValueError:
                print("❌ Invalid CGPA input.")
            return

    print("❌ Student with that Roll Number not found.")


def delete_student():
    roll = input("Enter Roll Number of the student to delete: ").strip()
    if not roll:
        print("❌ Roll Number cannot be empty.")
        return

    for student in students:
        if student['roll'] == roll:
            students.remove(student)
            print("✅ Student deleted successfully!")
            print("-" * 50) 
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
    view_students()
    print("-" * 50)

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
        view_students()
        print("-" * 50)
    else:
        print("❌ Invalid choice.")

def view_students():
    if not students:
        print("❌ No students to display.")
        return

    print("\n📋 List of Students:")
    print("-" * 50)
    print("{:<10} {:<20} {:<5} {:<10}".format("Roll", "Name", "CGPA", "Medal"))
    print("-" * 50)

    for s in students:
        medal_display = s['medal'] if s['medal'] else "-"
        print("{:<10} {:<20} {:<5} {:<10}".format(s['roll'], s['name'], s['cgpa'], medal_display))
    print("-" * 50)



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

def search_by_name(name):
    results = []
    for student in students:
        if student['name'].lower() == name.lower():
            results.append(student)

    return results

def binary_search_by_roll(roll):
    sorted_students = sorted(students, key=lambda s: s['roll'])
    left = 0
    right = len(sorted_students) - 1

    while left <= right:
        mid = (left + right) // 2
        if sorted_students[mid]['roll'] == roll:
            return sorted_students[mid]
        elif sorted_students[mid]['roll'] < roll:
            left = mid + 1
        else:
            right = mid - 1
    return None

def search_student():
    print("\n🔍 Search Student:")
    print("1. Search by Name (Linear Search)")
    print("2. Search by Roll Number (Binary Search)")
    
    choice = input("Enter choice (1 or 2): ")

    if choice == '1':
        name = input("Enter name to search: ")
        results = search_by_name(name)
        if results:
            print("\nFound student(s):")
            print("-" * 50)
            for s in results:
                print(f"Roll: {s['roll']}, Name: {s['name']}, CGPA: {s['cgpa']}")
        else:
            print("❌ No student found with that name.")
    
    elif choice == '2':
        roll = input("Enter roll number to search: ")
        result = binary_search_by_roll(roll)
        if result:
            print(f"\nFound: Roll: {result['roll']}, Name: {result['name']}, CGPA: {result['cgpa']}")
            print("-" * 50)
        else:
            print("❌ No student found with that roll number.")
    
    else:
        print("❌ Invalid choice.")

def assign_medals():
    if len(students) < 3:
        print("❌ Not enough students to assign medals (need at least 3).")
        return

    # First, sort students by CGPA in descending order
    sorted_students = sorted(students, key=lambda s: s['cgpa'], reverse=True)

    # Reset medals
    for student in students:
        student['medal'] = None

    # Assign medals to top 3
    sorted_students[0]['medal'] = '🥇 Gold'
    sorted_students[1]['medal'] = '🥈 Silver'
    sorted_students[2]['medal'] = '🥉 Bronze'

    print("🏅 Medals assigned to top 3 students based on CGPA!")
    print("-" * 50)

def show_menu():
    print("\n" + "=" * 50)
    print("🎓 Student CGPA Ranking System")
    print("=" * 50)
    print("1. Add Student")
    print("2. Update Student")
    print("3. Delete Student")
    print("4. Sort Students by CGPA")
    print("5. View All Students")
    print("6. Search Student")
    print("7. Assign Medals")
    print("8. Exit")
    print("=" * 50)



def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1–8): ").strip()

        if not choice:
            print("❌ Please enter a choice.")
            continue

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
            search_student()
        elif choice == '7':
            assign_medals()
        elif choice == '8':
            print("👋 Goodbye! Thanks for using the system.")
            print("=" * 50)
            break

        else:
            print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
