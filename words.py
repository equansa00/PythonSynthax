# # words.py

# def print_upper_words(words):
#     """Print each word from the list in uppercase."""
#     for word in words:
#         print(word.upper())

# # Test the function
# print_upper_words(["hello", "world", "python"])

# words.py

# def print_upper_words(words):
#     """Print each word from the list in uppercase."""
#     for word in words:
#         if word.startswith("e") or word.startswith("E"):
#             print(word.upper())

# # Test the function
# print_upper_words(["hello", "world", "python", "elephant"])

# words.py

def print_upper_words(words, must_start_with):
    """Print words from the list in uppercase if they start with a specified set of letters."""
    for word in words:
        if any(word.startswith(letter) for letter in must_start_with):
            print(word.upper())

# Test the function
print_upper_words(["hello", "world", "python", "elephant"],
                  must_start_with={"h", "e"})
