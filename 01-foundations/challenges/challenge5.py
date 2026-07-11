full_name = input("What is your full name? ")
#fstrings
print (f"Upper : {full_name}".upper())

print (f"Lower: {full_name}".lower())

#count = len(full_name)
#print(f"Letters:{count}")

#print(f"Letters: {len(full_name)}")

letters = full_name.replace(" ", "")
print(f"Letters: {len(letters)}")


print(f"First: {full_name.capitalize()[0]}")

print(f"Last: {full_name[-1]}")
