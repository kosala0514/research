def find_max(numbers):
    max_value = float('-inf') 

    for num in numbers:
        if num > max_value:
            max_value = num

    return max_value

numbers = [2, 7, 5, 9, 1]
max_value = find_max(numbers)
print(max_value)

