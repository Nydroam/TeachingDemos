import random

def convert(char, key):
    converted_char = ' '
    if char.isalpha():
        if char.islower():
            converted_char = chr((ord(char) - 97 + key) % 26 + 97) 
        else:
            converted_char = chr((ord(char) - 65 + key) % 26 + 65)
    return converted_char


while True:
    encrypted_sentence = ""
    sentence = input("Give me text to encrypt: \n")
    key = random.randint(1,25)
    for char in sentence:
        encrypted_sentence += convert(char, key)
        
    print(encrypted_sentence)
    print("Key: " + str(key))
