tuple_with_duplicates = (1, 2, 3, 2, 4, 5, 3, 6, 4)
unique_elements = tuple(set(tuple_with_duplicates))
print("Tuple without duplicates: ", unique_elements)