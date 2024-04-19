s=input("enter string: ")
n=''
for idx in range(len(s)):
    if s[idx].isnumeric():
        n=n+s[idx]
    if len(n)==10:
     print(n)
     n=""
