#week 3
#1.b
def encrypt(plaintext, key):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            # Encrypt uppercase letters
            if char.isupper():
                encrypted_text += chr((ord(char) + key - 65) % 26 + 65)
            # Encrypt lowercase letters
            else:
                encrypted_text += chr((ord(char) + key - 97) % 26 + 97)
        else:
            # Ignore non-alphabetic characters
            encrypted_text += char
    return encrypted_text

def decrypt(ciphertext, key):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            # Decrypt uppercase letters
            if char.isupper():
                decrypted_text += chr((ord(char) - key - 65) % 26 + 65)
            # Decrypt lowercase letters
            else:
                decrypted_text += chr((ord(char) - key - 97) % 26 + 97)
        else:
            # Ignore non-alphabetic characters
            decrypted_text += char
    return decrypted_text

def main():
    plaintext = input("Enter the plaintext: ")
    key = int(input("Enter the key (an integer value between 0 and 25): "))

    encrypted_text = encrypt(plaintext, key)
    print("Encrypted text:", encrypted_text)

    decrypted_text = decrypt(encrypted_text, key)
    print("Decrypted text:", decrypted_text)

if __name__ == "__main__":
    main()



#2.
def encrypt(plaintext, key):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            # Encrypt uppercase letters
            if char.isupper():
                encrypted_text += chr((ord(char) + key - 65) % 26 + 65)
            # Encrypt lowercase letters
            else:
                encrypted_text += chr((ord(char) + key - 97) % 26 + 97)
        else:
            # Ignore non-alphabetic characters
            encrypted_text += char
    return encrypted_text

def decrypt(ciphertext, key):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            # Decrypt uppercase letters
            if char.isupper():
                decrypted_text += chr((ord(char) - key - 65) % 26 + 65)
            # Decrypt lowercase letters
            else:
                decrypted_text += chr((ord(char) - key - 97) % 26 + 97)
        else:
            # Ignore non-alphabetic characters
            decrypted_text += char
    return decrypted_text

def main():
    plaintext = input("Enter the plaintext: ")
    key = int(input("Enter the key (an integer value between 0 and 25): "))

    encrypted_text = encrypt(plaintext, key)
    print("Encrypted text:", encrypted_text)

    decrypted_text = decrypt(encrypted_text, key)
    print("Decrypted text:", decrypted_text)

if __name__ == "__main__":
    main()

#3.
def encrypt(plaintext):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            # Encrypt uppercase letters
            if char.isupper():
                encrypted_text += chr(((ord(char) - 65) * 3 + 12) % 26 + 65)
            # Encrypt lowercase letters
            else:
                encrypted_text += chr(((ord(char) - 97) * 3 + 12) % 26 + 97)
        else:
            # Ignore non-alphabetic characters
            encrypted_text += char
    return encrypted_text

def decrypt(ciphertext):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            # Decrypt uppercase letters
            if char.isupper():
                decrypted_text += chr(((ord(char) - 12) * 9) % 26 + 65)
            # Decrypt lowercase letters
            else:
                decrypted_text += chr(((ord(char) - 12) * 9) % 26 + 97)
        else:
            # Ignore non-alphabetic characters
            decrypted_text += char
    return decrypted_text

def main():
    plaintext = input("Enter the plaintext: ")

    encrypted_text = encrypt(plaintext)
    print("Encrypted text:", encrypted_text)

    decrypted_text = decrypt(encrypted_text)
    print("Decrypted text:", decrypted_text)

if __name__ == "__main__":
    main()

#4.
import re

def generate_playfair_square(key):
    key = key.replace(" ", "").upper()
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # Note: 'J' is excluded
    key = re.sub(r'[^A-Z]', '', key)  # Remove non-alphabetic characters
    key = "".join(dict.fromkeys(key))  # Remove duplicates

    # Create the initial Playfair square
    square = ""
    for char in key:
        if char not in square:
            square += char
    for char in alphabet:
        if char not in square:
            square += char

    playfair_square = [square[i:i+5] for i in range(0, 25, 5)]
    return playfair_square

def find_char_positions(square, char):
    positions = []
    for i in range(5):
        for j in range(5):
            if square[i][j] == char:
                positions.append((i, j))
    return positions

def encrypt(plaintext, square):
    plaintext = re.sub(r'[^A-Z]', '', plaintext.upper())  # Remove non-alphabetic characters
    plaintext = re.sub(r'J', 'I', plaintext)  # Replace 'J' with 'I'
    if len(plaintext) % 2 != 0:
        plaintext += 'X'  # Add an extra character if the length is odd

    encrypted_text = ""
    for i in range(0, len(plaintext), 2):
        char1 = plaintext[i]
        char2 = plaintext[i+1]
        pos1 = find_char_positions(square, char1)
        pos2 = find_char_positions(square, char2)

        if pos1[0][0] == pos2[0][0]:
            encrypted_text += square[pos1[0][0]][(pos1[0][1] + 1) % 5]
            encrypted_text += square[pos2[0][0]][(pos2[0][1] + 1) % 5]
        elif pos1[0][1] == pos2[0][1]:
            encrypted_text += square[(pos1[0][0] + 1) % 5][pos1[0][1]]
            encrypted_text += square[(pos2[0][0] + 1) % 5][pos2[0][1]]
        else:
            encrypted_text += square[pos1[0][0]][pos2[0][1]]
            encrypted_text += square[pos2[0][0]][pos1[0][1]]

    return encrypted_text

def decrypt(ciphertext, square):
    decrypted_text = ""
    for i in range(0, len(ciphertext), 2):
        char1 = ciphertext[i]
        char2 = ciphertext[i+1]
        pos1 = find_char_positions(square, char1)
        pos2 = find_char_positions(square, char2)

        if pos1[0][0] == pos2[0][0]:
            decrypted_text += square[pos1[0][0]][(pos1[0][1] - 1) % 5]
            decrypted_text += square[pos2[0][0]][(pos2[0][1] - 1) % 5]
        elif pos1[0][1] == pos2[0][1]:
            decrypted_text += square[(pos1[0][0] - 1) % 5][pos1[0][1]]
            decrypted_text += square[(pos2[0][0] - 1) % 5][pos2[0][1]]
        else:
            decrypted_text += square[pos1[0][0]][pos2[0][1]]
            decrypted_text += square[pos2[0][0]][pos1[0][1]]

    return decrypted_text

def main():
    key = input("Enter the key: ").upper()
    plaintext = input("Enter the plaintext: ").upper()

    playfair_square = generate_playfair_square(key)
    encrypted_text = encrypt(plaintext, playfair_square)
    decrypted_text = decrypt(encrypted_text, playfair_square)

    print("Plaintext:", plaintext)
    print("Encrypted text:", encrypted_text)
    print("Decrypted text:", decrypted_text)

if __name__ == "__main__":
    main()

#5.
def generate_key(plaintext, key):
    key = list(key.upper())
    if len(plaintext) == len(key):
        return key
    else:
        for i in range(len(plaintext) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def encrypt(plaintext, key):
    encrypted_text = ""
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            shift = ord(key[i]) - 65
            if plaintext[i].isupper():
                encrypted_text += chr((ord(plaintext[i]) + shift - 65) % 26 + 65)
            else:
                encrypted_text += chr((ord(plaintext[i]) + shift - 97) % 26 + 97)
        else:
            encrypted_text += plaintext[i]
    return encrypted_text

def decrypt(ciphertext, key):
    decrypted_text = ""
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            shift = ord(key[i]) - 65
            if ciphertext[i].isupper():
                decrypted_text += chr((ord(ciphertext[i]) - shift - 65) % 26 + 65)
            else:
                decrypted_text += chr((ord(ciphertext[i]) - shift - 97) % 26 + 97)
        else:
            decrypted_text += ciphertext[i]
    return decrypted_text

def main():
    plaintext = input("Enter the plaintext: ")
    key = input("Enter the key: ")

    key = generate_key(plaintext, key)

    encrypted_text = encrypt(plaintext.upper(), key)
    decrypted_text = decrypt(encrypted_text, key)

    print("Plaintext:", plaintext)
    print("Encrypted text:", encrypted_text)
    print("Decrypted text:", decrypted_text)

if __name__ == "__main__":
    main()


#6.

def generate_key(plaintext, key):
    key = key.upper()
    if len(plaintext) == len(key):
        return key
    else:
        for i in range(len(plaintext) - len(key)):
            key += plaintext[i].upper()
    return key

def encrypt(plaintext, key):
    encrypted_text = ""
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            shift = ord(key[i]) - 65
            if plaintext[i].isupper():
                encrypted_text += chr((ord(plaintext[i]) + shift - 65) % 26 + 65)
            else:
                encrypted_text += chr((ord(plaintext[i]) + shift - 97) % 26 + 97)
            key += plaintext[i].upper()  # Append the current plaintext character to the key
        else:
            encrypted_text += plaintext[i]
    return encrypted_text

def decrypt(ciphertext, key):
    decrypted_text = ""
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            shift = ord(key[i]) - 65
            if ciphertext[i].isupper():
                decrypted_text += chr((ord(ciphertext[i]) - shift - 65) % 26 + 65)
            else:
                decrypted_text += chr((ord(ciphertext[i]) - shift - 97) % 26 + 97)
            key += decrypted_text[-1].upper()  # Append the current decrypted character to the key
        else:
            decrypted_text += ciphertext[i]
    return decrypted_text

def main():
    plaintext = input("Enter the plaintext: ")
    key = input("Enter the key: ")

    key = generate_key(plaintext, key)

    encrypted_text = encrypt(plaintext.upper(), key)
    decrypted_text = decrypt(encrypted_text, key)

    print("Plaintext:", plaintext)
    print("Encrypted text:", encrypted_text)
    print("Decrypted text:", decrypted_text)

if __name__ == "__main__":
    main()


#8.
def encrypt(plaintext, rails):
    rail_fence = [''] * rails
    direction = -1  # Direction of movement along the rails
    row = 0

    for char in plaintext:
        rail_fence[row] += char
        if row == 0 or row == rails - 1:
            direction *= -1
        row += direction

    return ''.join(rail_fence)

def decrypt(ciphertext, rails):
    rail_length = len(ciphertext)
    rail_fence = [''] * rails
    direction = -1
    row = 0

    for i in range(rail_length):
        rail_fence[row] += '*'

        if row == 0 or row == rails - 1:
            direction *= -1

        row += direction

    plaintext = ''
    index = 0

    for i in range(rails):
        for j in range(len(rail_fence[i])):
            if rail_fence[i][j] == '*' and index < rail_length:
                rail_fence[i] = rail_fence[i][:j] + ciphertext[index] + rail_fence[i][j + 1:]
                index += 1

    direction = -1
    row = 0

    for i in range(rail_length):
        plaintext += rail_fence[row][0]
        rail_fence[row] = rail_fence[row][1:]

        if row == 0 or row == rails - 1:
            direction *= -1

        row += direction

    return plaintext

def main():
    plaintext = input("Enter the plaintext: ")
    rails = int(input("Enter the number of rails: "))

    encrypted_text = encrypt(plaintext.upper(), rails)
    decrypted_text = decrypt(encrypted_text, rails)

    print("Plaintext:", plaintext)
    print("Encrypted text:", encrypted_text)
    print("Decrypted text:", decrypted_text)

if __name__ == "__main__":
    main()


#9.

def generate_key(plaintext, key):
    key_length = len(key)
    plaintext_length = len(plaintext)

    if key_length >= plaintext_length:
        return key[:plaintext_length]  # Truncate the key if it's longer than the plaintext

    # Repeat the key until its length matches or exceeds the length of the plaintext
    while len(key) < plaintext_length:
        key += key[:plaintext_length - len(key)]

    return key

def encrypt(plaintext, key):
    num_columns = len(key)

    # Construct the matrix
    matrix = [''] * num_columns
    for i in range(len(plaintext)):
        matrix[i % num_columns] += plaintext[i]

    # Encrypt by reading the columns in the order specified by the key
    encrypted_text = ''
    for col in key:
        col_index = int(col) - 1
        encrypted_text += matrix[col_index]

    return encrypted_text

def decrypt(ciphertext, key):
    num_columns = len(key)
    num_rows = len(ciphertext) // num_columns

    # Construct the matrix
    matrix = [[''] * num_rows for _ in range(num_columns)]
    k = 0
    for col in key:
        col_index = int(col) - 1
        for row in range(num_rows):
            matrix[col_index][row] = ciphertext[k]
            k += 1

    # Decrypt by reading the columns in the original order
    decrypted_text = ''
    for row in range(num_rows):
        for col in range(num_columns):
            decrypted_text += matrix[col][row]

    return decrypted_text.rstrip()  # Remove trailing padding

def main():
    plaintext = input("Enter the plaintext: ")
    key = input("Enter the key (column order, e.g., '2314' for 4 columns): ")

    key = generate_key(plaintext, key)

    encrypted_text = encrypt(plaintext.upper(), key)
    decrypted_text = decrypt(encrypted_text, key)

    print("Plaintext:", plaintext)
    print("Encrypted text:", encrypted_text)
    print("Decrypted text:", decrypted_text)

if __name__ == "__main__":
    main()




#10.

import math

def generate_grid(text, key):
    key_order = sorted(range(len(key)), key=lambda k: key[k])
    num_columns = len(key)
    num_rows = math.ceil(len(text) / num_columns)
    grid = [['' for _ in range(num_columns)] for _ in range(num_rows)]

    for i, char in enumerate(text):
        row = i // num_columns
        col = i % num_columns
        grid[row][key_order[col]] = char

    return grid

def encrypt(text, key):
    grid = generate_grid(text, key)
    encrypted_text = ''
    for col in range(len(key)):
        for row in range(len(grid)):
            encrypted_text += grid[row][col]
    return encrypted_text

def decrypt(encrypted_text, key):
    grid = generate_grid(encrypted_text, key)
    decrypted_text = ''
    for row in grid:
        decrypted_text += ''.join(row)
    return decrypted_text

def main():
    text = input("Enter the text to encrypt: ").replace(" ", "").upper()
    key = input("Enter the key for encryption: ").upper()

    encrypted_text = encrypt(text, key)
    print("Encrypted text:", encrypted_text)

    decrypted_text = decrypt(encrypted_text, key)
    print("Decrypted text:", decrypted_text)

if __name__ == "__main__":
    main()
