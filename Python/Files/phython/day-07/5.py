#WA function to take a string as parameter. Print its alternate characters starting from 2nd character
def stringaltprint(s):
    for idx in range(1,len(s),2):
        print(s[idx])
stringaltprint("abscdf")
