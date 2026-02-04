# caesar cypher. shifts letter X number of letters to encrypt it.
# decrypt does the reverse

def encrypt(word, cypher):
     # convert to ASCII value with ord(), apply shift, convert back to letter with chr()
     encrypted_word = ''
     for char in word:
         if 0 <= ord(char) - ord('a') <= 26
            position = ord(char) - ord('a')
            value = (position + cypher) % 26
            encrypted_word += chr(value)
        else:
            encrypted_word += char
     return encrypted_word

def decrypt(encrypted_word, cypher):
     decrypted_word = ''
     for char in encrypted_word:
         if 0 <= ord(char) - ord('a') <= 26
            position = ord(char) - ord('a')
            value = (position - cypher) % 26
            decrypted_word += chr(value)
        else:
            decrypted_word += char
     return decrypted_word

on = True
while on:
    method = input("Type 'encrypt', 'decrypt', or 'quit'\n").lower()
    if method == 'quit':
        on = False
        print("Goodbye")
        break
    user_word = input("What is the word you want to use?\n")

    if method == 'encrypt':
        cypher = int(input("What is the shift number?\n"))
        print(encrypt(user_word, cypher))
    elif method == 'decrypt':
        cypher = int(input("What is the shift number?\n"))
        print(decrypt(user_word, cypher))
    else:
        print("Please pick a valid option.")
        
