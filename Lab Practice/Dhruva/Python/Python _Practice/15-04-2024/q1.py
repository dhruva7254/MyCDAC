"""11. Given a paragraph count number of words, sentences. Every sentence ends with either . or ? or !
Print Count of how many normal sentences ending with . , how many interrogative sentences ( ending
with ?) and how many exclamatory sentences ( ending with !).
Ex.
Input : “I am at CDAC. What about you? I am surprised by current weather!”
Normal sentence : 1
Interrogative: 1
Exclamatory : 1"""

para="""I am at CDAC. What about you? I am surprised by current weather!"""
words=para.split()
print(len(words),words)
for word in words:
    if word[-1] == ".":
        Normal_sentence+=1
    elif word[-1] == ",":
        Interrogative+=1
    elif word[-1] == "!":
        Exvlamatory+=1
print(Normal_sentence,IInterrogative,Exvlamatory)
#para.count(.)
