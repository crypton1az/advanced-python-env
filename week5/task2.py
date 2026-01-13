import json

with open("students.json", "r", encoding="utf-8") as file:
    students = json.load(file)

for student in students:
    grades = student["grades"]
    total = 0

    for g in grades:
        total += g

    student["average"] = total / len(grades)

with open("students_updated.json", "w", encoding="utf-8") as file:
    json.dump(students, file, indent=4)
