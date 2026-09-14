python_students = {"Rahul", "Amit", "Priya"}
ml_students = {"Priya", "Amit", "Neha"}

# Students attending both
print(python_students & ml_students)

# All students
print(python_students | ml_students)

# Only Python students
print(python_students - ml_students)