students = [
    {"name": "Ahmed", "score": 85},
    {"name": "Bile", "score": 45},
    {"name": "Nimo", "score": 67}
]

for student in students:
    if student["score"] >= 60:
        print(f"{student['name']}: {student['score']} = Pass")
    else:
        print(f"{student['name']}: {student['score']} = Fail")
