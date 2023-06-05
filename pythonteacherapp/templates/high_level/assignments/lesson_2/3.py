sentence = input("Enter a sentence: ")
word_count = 0
is_word = False
for char in sentence:
    if char.isalnum():
        is_word = True
    elif is_word:
        word_count += 1
        is_word = False
if is_word:
    word_count += 1

print("Number of words:", word_count)
