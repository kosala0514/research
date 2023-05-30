sentence1 = "The quick brown fox jumps over the lazy dog."
sentence2 = "A quick brown dog jumps over the lazy fox."
words1 = set(sentence1.lower().split())
words2 = set(sentence2.lower().split())
common_words = words1.intersection(words2)
print(common_words)