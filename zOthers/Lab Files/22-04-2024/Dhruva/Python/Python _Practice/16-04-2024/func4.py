count=3
def hellofun():
    global count
    if count > 0:
        print("hello")
        count-=1
        hellofun()
    else:
        pass
print(hellofun())



def hello1fun(cnt):
    if cnt > 0:
        print("hello")
        hello1fun(cnt-1)
    else:
        pass
print(hello1fun(3))