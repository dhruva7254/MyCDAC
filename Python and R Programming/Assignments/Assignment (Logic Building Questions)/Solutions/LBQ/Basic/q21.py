

# 21) Find duplicate characters in a string.

def find_duplicate_characters(input_string):
    char_count = {}
    for char in input_string:
        char_count[char] = char_count.get(char, 0) + 1
    duplicates = [char for char, count in char_count.items() if count > 1]
    return duplicates

input_str = "hello world"
duplicates = find_duplicate_characters(input_str)
print("Duplicate characters:", duplicates)
