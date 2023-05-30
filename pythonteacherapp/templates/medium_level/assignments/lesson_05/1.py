a = 5
b = 3
operation = "add"

if operation == "add":
    result = a + b
elif operation == "subtract":
    result = a - b
elif operation == "multiply":
    result = a * b
elif operation == "divide":
    result = a / b
else:
    print("Invalid operation")

print("Result:", result)
