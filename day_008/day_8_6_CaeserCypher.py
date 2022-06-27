from replit import clear
clear()
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

"""
def encrypt(user_text,user_shift):
    encrypt_str = ""
    for letter in user_text:
        position = alphabet.index(letter)
        new_position = position + user_shift
        encrypt_str += alphabet[new_position]
    print(encrypt_str)

encrypt(user_text=text,user_shift=shift)
"""

"""_steps_
    1. Gather the user input 
    2. Index through with a for loop 
    3. Find the index of the alphabet 
    4. Take the shift number and move it in the alphabet 
    5. Keep that same index value and add the shift number
"""
"""
    _steps_
    
"""        

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
"""
def decrypt(user_text,user_shift):
    decrypt_str = ""
    for letter in user_text:
        position = alphabet.index(letter)
        new_position = position - user_shift
        decrypt_str += alphabet[new_position]
    print(decrypt_str)
"""
## decrypt(user_text=text,user_shift=shift)
  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.

def encrypt_decrypt(user_text,user_shift,user_dir):
    encrypt_str = ""
    if user_dir == "decode":
        for letter in user_text:
            position = alphabet.index(letter)
            ##user_shift *= -1
            new_position = position + (user_shift*-1)    
            encrypt_str += alphabet[new_position]
        print(encrypt_str)
    elif user_dir == "encode":
        for letter in user_text:
            position = alphabet.index(letter)
            new_position = position + user_shift    
            encrypt_str += alphabet[new_position]
        print(encrypt_str)
    else: 
        print("not an option try again")
        


encoding_text = True
while encoding_text != False:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt or 'end' to exit:\n")
    if direction == "end":
        print("goodbye")
        encoding_text = False
        exit
    else: 
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        encrypt_decrypt(user_text=text,user_shift=shift,user_dir=direction)
