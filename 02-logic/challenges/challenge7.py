number =int(input("Number: "))

if number%2==0:
  print(f"Number: {number}")
  print(f"{number} is eveen")
  print("Even numners: ")
  for i in range(2, number):
    if i % 2 == 0:
        print(i)
  
else:
  print(f"Number:{number}")
  print(f"{number} is odd")
  print("Odd Numbers:")
  for i in range(1, number):
    if i % 2 != 0:
        print(i)

