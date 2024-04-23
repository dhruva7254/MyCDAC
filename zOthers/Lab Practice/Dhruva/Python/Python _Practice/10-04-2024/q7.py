counter=0
while(counter<5):
    print("""menu:    """)
    item=input()
    if(item=='q'):
        break
    counter +=1
else:
    print("Limit Reached!")    
    print("complete!")
