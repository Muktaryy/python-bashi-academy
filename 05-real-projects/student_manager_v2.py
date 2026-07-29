
students = [
    {"name": "Ahmed", "score": 80},
    {"name": "Hodan", "score": 45},
    {"name": "Bile", "score": 90},
    {"name": "Nimo", "score": 55}
]

print("Student Manager")

print("1. Show all students")
print("2. Search student")
print("3. Add student")
print("4. Remove student")
print("5. Show statistics")
print("6. Exit")

choose = int(input("Choose Option: "))

if choose == 1:
    for student in students:
        print(f"{student['name']}: {student['score']}")

elif choose == 2:
    search = input("Search Student: ")

    found = False

    for student in students:
        if search == student["name"]:
            print(f"Found: {student['name']} - {student['score']}")
            found = True

    if not found:
        print("Student not found")

elif choose == 3:
    name = input("Enter student name: ")
    score = int(input("Enter student score: "))

    new_student = {"name": name, "score": score}

    students.append(new_student)

    print("Student added successfully!")

elif choose == 4:
    remove_student = input("Remove Student: ")

    found = False

    for student in students:
        if remove_student == student["name"]:
            students.remove(student)
            print(f"{remove_student} removed successfully!")
            found = True
            break

    if not found:
        print("Student not found")

elif choose == 5:
    passed = 0
    failed = 0
    total = 0
    highest = students[0]
    lowest = students[0]

    for student in students:

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

elif choose == 6:
    print("Goodbye!")
