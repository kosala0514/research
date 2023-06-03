user_input = input("Enter a string: ")
uppercase_string = ""
for char in user_input:
    if 'a' <= char <= 'z':
        uppercase_string += chr(ord(char) - 32)
    else:
        uppercase_string += char
print("Uppercase string:", uppercase_string)
