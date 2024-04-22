
def minion_game(string):
    kevin_score = 0
    stuart_score = 0
    vowels ='AEIOU'
    
    for i in range(len(string)):
        if string[i] in vowels: 
            kevin_score += (len(string)-i)
        else:
            stuart_score += (len(string)-i)
    
    # print("kevin",kevin_score)

    if kevin_score > stuart_score:
        print("Kevin",kevin_score)
    elif kevin_score < stuart_score:
        print("Stuart",stuart_score)
    else:
        print("Draw")

a = input("Enter the String: ")
minion_game(a)


    
