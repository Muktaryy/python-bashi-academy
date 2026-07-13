day=input("Enter Day? ").lower().strip()
price=float(input("Enter price? "))

first_discount= 20/100
second_discount= 10/100

if (day=="monday" or day=="friday"):
  print(f"Day: {day.capitalize()}")
  print(f"Price: ${price}")
  print(f"Discount:20%")
  first_total=price * (1 - first_discount)
  print(f"Final: ${first_total:.2f}")

elif (day=="wednesday"):
  print(f"Day: {day.capitalize()}")
  print(f"Price: ${price}")
  print(f"Discount:10%")
  first_total=price * (1 - second_discount)
  print(f"Final: ${first_total:.2f}")


else:
  print(f"Day: {day.capitalize()}")
  print(f"Price: ${price}")
  print(f"Discount:0%")
  print(f"Final:${price}")

