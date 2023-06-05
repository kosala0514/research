input_list = input("Enter a list of numbers, separated by spaces: ").split()

input_list = [int(num) for num in input_list]

for i in range(len(input_list)):
    if input_list[i] % 2 == 0:
        input_list[i] = 0

print("Updated list: ", input_list)
