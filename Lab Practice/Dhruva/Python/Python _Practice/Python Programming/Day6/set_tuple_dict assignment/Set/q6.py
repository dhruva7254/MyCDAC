"""6. Take a sentence as input from user. Every word is seperated by space. 
Print all unique words from the sentence."""

sentence = input("Enter a sentence: ")
unique_words = set(sentence.split())
print("Unique words:", unique_words)
