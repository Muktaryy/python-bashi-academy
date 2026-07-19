# number to text coverter
print("")
print("")
print("")

print("Waxaa la ogolyahy kaliya inta udhaxaysa 1 ilaa 10?")

user_input = int(input(" Fadlan gali lambarka = "))

def ubadalqoral(lambar):
    ones = ["", "one", "laba", "sadex", "afar",
            "shan", "lix", "todoba", "sideed",
            "sagaal", "toban"]
    if 1<= lambar <= 10:
        return ones[lambar]

    else:
        return ("Fadlan geli inta udhexaysa 1 ilaa 10")

natiijada = ubadalqoral(user_input)
print(f"Natiijada = {natiijada}")
