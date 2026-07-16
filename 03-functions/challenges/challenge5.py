def ticket_price(age):
    if age < 12:
        return "$5"
    elif age <= 17:
        return "$8"
    else:
        return "$12"

print("Age 10:", ticket_price(10))

print("Age 15:", ticket_price(15))

print("Age 25:", ticket_price(25))
