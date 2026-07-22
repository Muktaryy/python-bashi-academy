items = []

item = input("Add item: ")

while item != "done":
    items.append(item)
    item = input("Add item: ")

for i in range(len(items)):
    print(f"{i + 1}. {items[i]}")

print(f"Total: {len(items)}")
