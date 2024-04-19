#WA function to take list of strings as parameter and print all strings which have character 's' 2 times
def function8(l:list):
    for e in l:
        if e.count("s")==2:
            print(e)
l1=["asd","ads","sas","sds","abc",""]
function8(l1)