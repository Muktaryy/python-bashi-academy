name = input("What is you rname? ")
age = int(input("how old are you? "))
weight= float(input("What is your bag wieght? "))

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Bag weight: {weight}")

if age>= 18 and weight <= 23:
    print("Boarding pass")
    print(f"Passenger: {name}")
    print(f"Status: checked in")
elif age<= 18 and weight >= 23:
    print("Boarding fialed")
    print(f"Passenger: {name}")
    print(f"Status: you most be 18 to fly alone and bag most be under 23 wegiht")

elif age<=17:
    print(f"Passenger: {name}")
    print("Boarding failed")
    print(f"Status: You must be 18 to fly alone")
elif  weight >=24:
    print("Boarding failed")
    print(f"Passenger: {name}")
    print(f"Status: Bag most be under 23")

