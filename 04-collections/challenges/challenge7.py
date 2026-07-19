contacts= { 
  "name": "Ahmed", 
  "phone" : 98765432,}

name= input("Enter Your name? ").capitalize()
if (name == "Ahmed"):
  print(f"Search: {name} ")
  print(f"Ahmed: {contacts['phone']}")
else:
  print("Not found")
