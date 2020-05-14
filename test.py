alphabet_pos = {'A':0, 'a':0, 'B':1, 'b':1, 'C':2, 'c':2, 'D':3, 'd':3,
'E':4, 'e':4, 'F':5, 'f':5, 'G':6, 'g':6, 'H':7, 'h':7, 'I':8, 'i':8,
'J':9, 'j':9, 'K':10, 'k':10, 'L':11, 'l':11, 'M':12, 'm':12, 'N': 13,
'n':13, 'O':14, 'o':14, 'P':15, 'p':15, 'Q':16, 'q':16, 'R':17, 'r':17,
'S':18, 's':18, 'T':19, 't':19, 'U':20, 'u':20, 'V':21, 'v':21, 'W':22,
'w':22, 'X':23, 'x':23, 'Y':24, 'y':24, 'Z':25, 'z':25 }

def alphabet_position(letter):
    alphabet_pos = {'A':0, 'a':0, 'B':1, 'b':1, 'C':2, 'c':2, 'D':3,
'd':3, 'E':4, 'e':4, 'F':5, 'f':5, 'G':6, 'g':6, 'H':7, 'h':7, 'I':8,
'i':8, 'J':9, 'j':9, 'K':10, 'k':10, 'L':11, 'l':11, 'M':12, 'm':12,
'N': 13, 'n':13, 'O':14, 'o':14, 'P':15, 'p':15, 'Q':16, 'q':16,
'R':17, 'r':17, 'S':18, 's':18, 'T':19, 't':19, 'U':20, 'u':20, 'V':21,
'v':21, 'W':22, 'w':22, 'X':23, 'x':23, 'Y':24, 'y':24, 'Z':25, 'z':25
}
    pos = alphabet_pos[letter]
    return pos

def rotate(letter, rot):
    shift = 97 if letter.islower() else 65
    return chr((ord(letter) + rot - shift) % 26 + shift)

def encrypt(text, key):
    encrypted = []    
    starting_index = 0
    for letter in text:
    # if it's alphanumerical, keep it that way
    # find alphabet position
        rotation = alphabet_position(key[starting_index])
    # if it's a space or non-alphabetical character, append and move on
        if not letter in alphabet_pos:
            encrypted.append(letter)
        elif letter.isalpha():            
            encrypted.append(rotate(letter, rotation))             

    #if we've reached last index, reset to zero, otherwise + by 1
        if starting_index == (len(key) - 1): 
            starting_index = 0
        else: 
            starting_index += 1

    return ''.join(encrypted)    

text = input("Enter some text:")
key = input("Enter a key:")

print(encrypt(text,key))