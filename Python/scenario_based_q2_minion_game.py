
# Problem 2:

# Ravi and Lata want to play the 'The Minion Game'.

# Game Rules

# Both players are given the same string s.

# Both players have to make substrings using the letters of the string s.

# Ravi has to make words starting with consonants.

# Lata has to make words starting with vowels.

# The game ends when both players have made all possible substrings.

# Scoring

# A player gets +1 point for each occurrence of the substring in the string s.

# For Example:
# String  s = BANANA

# Ravi's vowel beginning word = ANA

# Here, ANA occurs twice in BANANA. Hence, ravi will get 2 Points.

# Only aeiou are considered as vowels here

# Print name of winner the score of the winner

# In case draw print names of both and score

# ref: Hacker rank 'the-minion-game'
# https://www.hackerrank.com/challenges/the-minion-game/problem

def minion_game(s):
    vowels = 'AEIOU'
    ravi_score = 0
    lata_score = 0
    length = len(s)

    for i in range(length):
        if s[i] in vowels:
            lata_score += length - i
        else:
            ravi_score += length - i

    if ravi_score > lata_score:
        print("Ravi", ravi_score)
    elif lata_score > ravi_score:
        print("Lata", lata_score)
    else:
        print("Draw", ravi_score)

# Example usage:
s = "BANANA"
minion_game(s)
