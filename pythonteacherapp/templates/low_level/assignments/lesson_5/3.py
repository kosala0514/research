input_string = input("Enter a string: ")
result = ""
for char in input_string:
    if char == 'a':
         result += 'b'
    else:
        result += char


print("Output string:", result)
