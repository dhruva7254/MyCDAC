# Q WA function to take list of strings as parameter and print all strings which have character 's' 2 times

def cha2tim(a:list):
    for i in a:
        if i.count('s')==2:
            b=print(i)
        else:
            b=0
    return b
c=['cassandra','spoilers','stars']
cha2tim(c)

