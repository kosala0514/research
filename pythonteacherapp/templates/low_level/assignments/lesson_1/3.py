string = input("Enter a string: ")
reversed_string = ""
index = len(string) - 1

while index >= 0:
    reversed_string += string[index]
    index -= 1
print("Reversed string:", reversed_string)
