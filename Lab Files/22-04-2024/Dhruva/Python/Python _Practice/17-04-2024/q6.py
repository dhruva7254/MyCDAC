
# WAP to find unique characters in a sentence and count their occurance.

sent = 'IACSD has brilliant students'
sent=sent.lower()
unique_char = set(sent.lower())
print(unique_char)
char_count={}
for char in unique_char:
    char_count[char] = sent.count(char)
print(char_count)

