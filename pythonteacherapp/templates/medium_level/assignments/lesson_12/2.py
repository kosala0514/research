import random

def generate_random_number(minimum, maximum):
    return random.randint(minimum, maximum)

minimum_value = 1
maximum_value = 10
random_number = generate_random_number(minimum_value, maximum_value)
print(random_number)
