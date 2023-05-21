size = input("Enter the size of the pizza (S, M, L): ")
toppings = input("Enter the toppings (separated by commas): ")

if size == "S":
    cost = 8.99
elif size == "M":
    cost = 10.99
elif size == "L":
    cost = 12.99
else:
    print("Invalid size entered!")
    exit()

if "pepperoni" in toppings:
    cost += 1  

print("Total cost: $", cost)
