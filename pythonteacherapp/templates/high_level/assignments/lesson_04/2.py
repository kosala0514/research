num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

sum_result = num1 + num2
print("Sum: ", sum_result)

diff_result = num1 - num2
print("Difference: ", diff_result)

prod_result = num1 * num2
print("Product:", prod_result)

if num2 != 0:
    quot_result = num1 / num2
    print("Quotient:", quot_result)
else:
    print("Cannot divide by zero.")
