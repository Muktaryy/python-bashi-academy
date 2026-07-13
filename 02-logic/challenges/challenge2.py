age = int(input("How old are you? "))

if (age <12):
    print(f"Age: {age}")
    print(f"Ticket: $5")
elif(age >=12 and 17):
    print(f"Age: {age}")
    print("Ticket: $8")
elif(age >18):
    print(f"Age: {age}")
    print(f"Ticket: 12")
