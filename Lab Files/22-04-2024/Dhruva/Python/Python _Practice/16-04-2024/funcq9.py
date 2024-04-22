# Q WA function to take list of dictionaries. Print all dictionaries which contain key "id".

def pridict(a:list):
    for i in a:
        if 'id' in i:
            print(i)
    # else:
    #     b=0
    # #return b
c=[{1:10,'name':'car',3:30,'rollno':100,5:50},{2:20,'id':45,4:40}]
pridict(c)