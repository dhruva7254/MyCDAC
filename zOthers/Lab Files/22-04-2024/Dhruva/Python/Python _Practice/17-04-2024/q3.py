# WAP to check if an array of integers contains three increasing adjacent numbers
#     ex. [1,3,5,2,5] --> True
#         [1,1,4,2,67,5] --> False
#         [1,9,2,67,100,124,34] --> True

num=int(input('enter length of list: '))
h=[]
for i in range(1,num+1):
    h.append(int(input('enter list values : ')))
# print(h)
for i in range(len(h)-2):
    if (h[i+1] > h[i]) and (h[i+2] > h[i+1]):
        print(h,"--> True")
        break
    else:
        print(h,"--> False")
        break

