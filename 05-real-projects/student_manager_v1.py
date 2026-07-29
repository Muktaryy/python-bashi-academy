students = [
    {"name": "Ahmed", "score": 80},
    {"name": "Hodan", "score": 45},
    {"name": "Bile", "score": 90},
    {"name": "Nimo", "score": 55}
]

passed = 0
failed = 0
highest = students[0]
lowest = students[0]
total = 0

for student in students:
    print(f"{student['name']}: {student['score']}")

    total = total + student["score"]

    if student["score"] >= 60:
        passed = passed + 1
    else:
        failed = failed + 1

    if student["score"] > highest["score"]:
        highest = student

    if student["score"] < lowest["score"]:
        lowest = student

average = total / len(students)

print(f"Passed students: {passed}")
print(f"Failed students: {failed}")
print(f"Highest Student: {highest['name']} - {highest['score']}")
print(f"Lowest Student: {lowest['name']} - {lowest['score']}")
print(f"Average Score: {average}")
