#6. Take a sentence as input from user. Every word is seperated by space. Print all unique words from the sentence.
s='test my test'
l1=s.split(" ")
#s1={e for e in l1}
#for e in set(s1):
#    print(e)
l2=[]
for e in l1:
    if e not in l2:
        l2.append(e)
for e in l2:
    print(e)    