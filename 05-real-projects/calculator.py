# AYnu samaynu xisaabiye

print("")
print("Maxaynu samaynaa? ")
print(" B: Isku dar")
print(" T: Kalajar ")
print(" J: isku dhufo")
print(" X: kal qaybi ")

dooro = input("Dooro = ").upper()

number1=int(input("Fadlan geli Lambarka hore  = "))
number2=int(input("Fadlan geli Lambarka danbe = "))

def add(a,b):
    print(f"Natiijadu waa: {a+b}")
def subtract(a,b):
    print(f"Natiijadu waa: {a-b}")
def multiply(a,b):
    print(f"Natiijadu waa: {a*b}")
def divide(a,b):
    print(f"Natiijadu waa: {a/b}")

if (dooro == "B"):
    add(number1,number2)
elif (dooro == "T"):
    subtract(number1,number2)
elif (dooro == "J"):
    multiply(number1,number2)
elif (dooro == "X"):
    divide(number1,number2)
else:
    print("Waxaad dooratay xisaabiye khaldan")
    print("Fadlan hubi inaad dooratay ( B, T, J , X")
    print("Wixii ka baxsan ( B, T, J , X.) Waa khalad")
