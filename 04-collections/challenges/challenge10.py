products = [
    {"name": "Laptop", "price": 999},
    {"name": "Phone", "price": 699},
    {"name": "Headphones", "price": 149}
]

search = input("Search: ")

found = False

for product in products:
    if product["name"] == search:
        print(f"{product['name']}: ${product['price']}")
        found = True

if found == False:
    print("Not found.")
