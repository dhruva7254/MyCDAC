s=input("enter sering: ")
w=int(input("enter width: "))
for idx in range((len(s)//w+1)):
    sf=s[0:w]
    s=s[w:len(s)]
    print(sf)