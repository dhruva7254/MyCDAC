# Q WA function to take a string as parameter. Print its alternate characters starting from 2nd character

def altcha(a:str):
    b=a[1::2]
    return b
c=str(input('Enter a string: '))
print(altcha(c))