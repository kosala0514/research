menu = [
    {'name': 'Sandwich', 'description': 'Description of item 1', 'price': 50},
    {'name': 'Juice', 'description': 'Description of item 2', 'price': 200},
    {'name': 'Fried Rice', 'description': 'Description of item 3', 'price': 950}
]

for item in menu:
    print(f"Name: {item['name']}")
    print(f"Description: {item['description']}")
    print(f"Price: ${item['price']}\n")

new_item = {'name': 'Burger', 'description': 'Description of item 4', 'price': 10.99}
menu.append(new_item)

for item in menu:
    print(f"Name: {item['name']}")
    print(f"Description: {item['description']}")
    print(f"Price: ${item['price']}\n")

menu.pop(1)

for item in menu:
    print(f"Name: {item['name']}")
    print(f"Description: {item['description']}")
    print(f"Price: ${item['price']}\n")
