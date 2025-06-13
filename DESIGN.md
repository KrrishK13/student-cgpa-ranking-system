# 🧠 Design – Student CGPA Ranking System

## 👤 Student Details

Each student will have:
- Roll number (e.g., 101)
- Name (e.g., Mahesh)
- CGPA (e.g., 9.0)

All students will be stored in a list like this:

```python
students = [
    {"roll": "101", "name": "Mahesh", "cgpa": 9.0},
    {"roll": "102", "name": "Aditi", "cgpa": 8.7}
]

## 📋 Menu Options (CLI)

The program will show a menu with:

1. Add Student  
2. Update Student  
3. Delete Student  
4. View All Students  
5. Search Student  
6. Sort Students by CGPA  
7. Assign Medals  
8. Exit

## ⚙️ Planned Functions

Each menu option will run a function:

- `add_student()`  
- `update_student()`  
- `delete_student()`  
- `view_students()`  
- `search_student()`  
- `sort_students()`  
- `assign_medals()`