import random

array = [random.randint(1, 100) for _ in range(15)]

print("Array: ", array)

smallest = min(array)
largest = max(array)

print("Smallest number: ", smallest)
print("Largest number: ", largest)
