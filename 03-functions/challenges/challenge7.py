def is_adult(age):
    if age >=18:
        return (f"{age}: True")
    else:
       return (f"{age}: False")

print(is_adult(12))
print(is_adult(18))
print(is_adult(25))
