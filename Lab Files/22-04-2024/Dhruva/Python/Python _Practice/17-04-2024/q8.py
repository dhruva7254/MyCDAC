

# WAP to find unique characters in a sentence and count their occurance.

sent = 'IACSD has brilliant students'
sent=sent.lower()
words = sent.split()
# unique_char = set(sent.lower())
# print(unique_char)
word_count={}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)

