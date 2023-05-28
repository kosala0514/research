numbers = [1, 2, 3, 4, 5]
square_lambda = lambda x: x ** 2

squared_numbers = list(map(square_lambda, numbers))
print(squared_numbers)
