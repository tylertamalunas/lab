# caesar cypher. shifts letter X number of letters to encrypt it.
# decrypt does the reverse

def encrypt(word, cypher):
     # convert to ASCII value with ord(), apply shift, convert back to letter with chr()
    encrypted_word = ''
    for char in word:
        if 0 <= ord(char) - ord('a') <= 25:
            position = ord(char) - ord('a')
            new_char = (position + cypher) % 26
            encrypted_word += chr(new_char + ord('a'))
        elif 0 <= ord(char) - ord('A') <= 25:
            position = ord(char) - ord('A')
            new_char = (position + cypher) % 26
            encrypted_word += chr(new_char + ord('A'))
        else:
            encrypted_word += char
    print(encrypted_word)

def decrypt(encrypted_word, cypher):

    decrypted_word = ''
    for char in encrypted_word:
        if 0 <= ord(char) - ord('a') <= 25:
            position = ord(char) - ord('a')
            new_char = (position - cypher) % 26
            decrypted_word += chr(new_char + ord('a'))
        elif 0 <= ord(char) - ord('A') <= 25:
            position = ord(char) - ord('A')
            new_char = (position - cypher) % 26
            encrypted_word += chr(new_char + ord('A'))
        else:
            decrypted_word += char
    print(decrypted_word)

on = True
while on:
    method = input("Type 'encrypt', 'decrypt', or 'quit'\n").lower()
    if method == 'quit':
        on = False
        print("Goodbye")
        break

    user_word = input("Type your message:\n")
    cypher = int(input("What is the shift number?\n"))

    if method == 'encrypt':
        encrypt(user_word, cypher)
    elif method == 'decrypt':
        decrypt(user_word, cypher)
    else:
        print("Please pick a valid option.")
        
