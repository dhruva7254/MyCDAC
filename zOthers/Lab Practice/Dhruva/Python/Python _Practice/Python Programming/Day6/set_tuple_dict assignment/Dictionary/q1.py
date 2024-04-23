"""1. In cryptography, a Caesar cipher is a very simple encryption techniques in which each letter in the 
plain text is replaced by a letter some fixed number of positions down the alphabet. For example, with a 
shift of 3, A would be replaced by D, B would become E, and so on. The method is named after Julius Caesar, 
who used it to communicate with his generals. ROT-13 ("rotate by 13 places") is a widely used example of a 
Caesar cipher where the shift is 13. In Python, the key for ROT-13 may be represented by means of the 
following dictionary
{'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 'i':'v', 'j':'w', 'k':'x', 'l':'y', 
'm':'z', 'n':'a', 'o':'b', 'p':'c', 'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k', 
'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S', 'G':'T', 'H':'U', 'I':'V', 'J':'W', 
'K':'X', 'L':'Y', 'M':'Z', 'N':'A', 'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I', 
'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}
Your task in this exercise is to implement an encoder/decoder of ROT-13. Once you're done, you will be able 
to read the following secret message:
Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!
Note that since English has 26 characters, your ROT-13 program will be able to both encode and decode texts 
written in English."""

# def caesar_cipher(text, shift):
#     result = ""
#     for char in text:
#         if char.isalpha():
#             if char.islower():
#                 result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
#             else:
#                 result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
#         else:
#             result += char
#     return result

# encoded_text = caesar_cipher("Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!", 13)
# print("Decoded text:", encoded_text)

# text="Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!"
# shift=13

# encoded_text=result
# print("Decoded text:", encoded_text)

"""def caesar_cipher(char):
    # Define the ROT-13 dictionary
    rot13_dict = {
        'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 'i':'v', 'j':'w',
        'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c', 'q':'d', 'r':'e', 's':'f', 't':'g',
        'u':'h', 'v':'i', 'w':'j', 'x':'k', 'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q',
        'E':'R', 'F':'S', 'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A',
        'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I', 'W':'J', 'X':'K',
        'Y':'L', 'Z':'M'
    }
    
    # Check if the character is in the ROT-13 dictionary
    if char in rot13_dict:
        return rot13_dict[char]
    else:
        return char

# Define the secret message
secret_message = "Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!"

# Decode the secret message using ROT-13
decoded_message = ''.join(map(caesar_cipher, secret_message))

# Print the decoded message
print("Decoded message:", decoded_message)"""


# rot13_dict = {
#         'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 'i':'v', 'j':'w',
#         'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c', 'q':'d', 'r':'e', 's':'f', 't':'g',
#         'u':'h', 'v':'i', 'w':'j', 'x':'k', 'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q',
#         'E':'R', 'F':'S', 'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A',
#         'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I', 'W':'J', 'X':'K',
#         'Y':'L', 'Z':'M'
#     }
# if char in rot13_dict:
#     caesar_cipher=rot13_dict[char]
# else:
#     caesar_cipher=char
# secret_message = "Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!"
# decoded_message = ''.join(map(caesar_cipher, secret_message))
# print("Decoded message:", decoded_message)


"""# Define the secret message
secret_message = "Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!"

# Define the ROT-13 dictionary
rot13_dict = {
    'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 'i':'v', 'j':'w',
    'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c', 'q':'d', 'r':'e', 's':'f', 't':'g',
    'u':'h', 'v':'i', 'w':'j', 'x':'k', 'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q',
    'E':'R', 'F':'S', 'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A',
    'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I', 'W':'J', 'X':'K',
    'Y':'L', 'Z':'M'
}

# Decode the secret message using ROT-13
decoded_message = ''.join(map(lambda char: rot13_dict[char] if char in rot13_dict else char, secret_message))

# Print the decoded message
print("Decoded message:", decoded_message)"""


