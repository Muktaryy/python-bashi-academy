name= input("What is your name? ")
destination= input("Which city are you going to? ")
day=int(input("How many days? "))

print(f"Traveler: {name.upper()}")
print(f"Destination: {destination.capitalize()}")
print(f"Days: {day}")

print(f"Note: {name.capitalize()} is spending {day} days in {destination}. Bon voyage!")
