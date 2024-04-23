
# WAP to find unique characters in a sentence and count their occurance.

sent = 'IACSD has brilliant students'
sent=sent.lower()
# unique_char = set(sent.lower())
# print(unique_char)
char_count={}
for char in sent:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
print(char_count)

