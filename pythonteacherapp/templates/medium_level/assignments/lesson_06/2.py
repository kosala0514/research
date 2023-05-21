input_strings = ['Hello', 'Python', 'World']
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
new_strings = []

for string in input_strings:
    new_string = ""
    for char in string:
        if char not in vowels:
            new_string += char
    new_strings.append(new_string)
print(new_strings)