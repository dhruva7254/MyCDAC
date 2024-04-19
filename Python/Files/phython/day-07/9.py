#WA function to take list of dictionaries. Print all dictionaries which contain key "id"
def function9(l:list):
    for e in l:
        for key in e:
            if key=="id":
                print(e)
l1=[{"id":2},{"t":"j",1:2,2:2},{"id":2,1:2},{1:2,2:3}]             
function9(l1)