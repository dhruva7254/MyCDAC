
# stars :: start =1, increase by 2, 
#         end= no of lines
# spaces :: start = no of lines // 2
#            decrease by 1
#            end =0

n= int(input("Enter no of lines"))
count=0 
stars=1
spaces=n//2
while(count < (n//2 +1)):
    print(" "*spaces,"*"*stars,sep="")
    spaces=spaces-1 #spaces -=1
    stars= stars+2 # stars +=2
    count+=1
count=0
stars=n-2
spaces = 1
while(count < (n//2)):
    print(" "*spaces,"*"*stars,sep="")
    spaces=spaces+1 #spaces +=1
    stars= stars-2 # stars -=2
    count+=1



# var1=10
# for idx in range(1,6): # 1,2,3,4,5
#     print("*"*idx)
"""
*
**
***
****
*****
"""


