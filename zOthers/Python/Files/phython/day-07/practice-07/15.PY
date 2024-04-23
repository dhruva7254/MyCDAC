#15. Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated 
#sequence after sorting them alphabetically. 
#Sample Items : green-red-yellow-black-white
#Expected Result : black-green-red-white-yellow
def functionp15(s:str):
    s=s.split("-")
    s.sort(reverse=False)
    s="-".join(e for e in s)
    print(s)
s="green-red-yellow-black-white"
functionp15(s)