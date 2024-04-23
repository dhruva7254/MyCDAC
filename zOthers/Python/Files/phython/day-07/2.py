#WA function to take list as parameter and print all numbers of given list which are divisible by 11
def listdiv11(l:list):
    for e in l:
        if e%11==0:
            print(e)
listdiv11([22,33,21,20])            