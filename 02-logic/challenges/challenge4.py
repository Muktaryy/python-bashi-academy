limit = int(input("limit? "))
speed = int(input("Speed? "))

over_limit = speed - limit
fine = (over_limit // 10) * 50

if speed > limit:
    print(f"Speed limit: {limit}")
    print(f"Your speed: {speed}")
    print(f"Over by: {over_limit} km/h")
  
    print(f"Fine: ${fine}")
else:
    print("No fine.")
