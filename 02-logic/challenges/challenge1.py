age = int(input("how old are you? "))

if (age >= 18):
    print("You can vote")

else:
    vote = 18-age # sanadka uu codayn karo
    print(f"You can't vote yet. {vote} years more!")
