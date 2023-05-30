import random

array = [random.randint(1, 100) for _ in range(20)]

even_sum = sum(num for num in array if num % 2 == 0)

print("Array:", array)
print("Sum of even numbers:", even_sum)
