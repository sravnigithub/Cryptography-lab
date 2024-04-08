#week 2 Encrypt the message “PAY” using hill cipherwith the following keymatrix
 # and show the decryption to formulate original plaintext K
import numpy as np

def hill_cipher_encrypt(plaintext, key_matrix):
    # Convert plaintext to numbers
    plaintext = [ord(char) - 65 for char in plaintext.upper()]
    # Padding if necessary
    if len(plaintext) % len(key_matrix) != 0:
        padding = len(key_matrix) - (len(plaintext) % len(key_matrix))
        plaintext.extend([23] * padding)  # Adding 'X' as padding
    # Reshape plaintext into a matrix
    plaintext_matrix = np.array(plaintext).reshape(-1, len(key_matrix))
    # Perform encryption
    ciphertext_matrix = np.dot(plaintext_matrix, key_matrix) % 26
    # Convert numbers to letters
    ciphertext = ''.join([chr(char + 65) for sublist in ciphertext_matrix.tolist() for char in sublist])
    return ciphertext

def hill_cipher_decrypt(ciphertext, key_matrix):
    # Convert ciphertext to numbers
    ciphertext = [ord(char) - 65 for char in ciphertext.upper()]
    # Reshape ciphertext into a matrix
    ciphertext_matrix = np.array(ciphertext).reshape(-1, len(key_matrix))
    # Find the modular multiplicative inverse of the key matrix
    inverse_matrix = np.linalg.inv(key_matrix)
    determinant = int(round(np.linalg.det(key_matrix)))
    # Find the multiplicative inverse of the determinant modulo 26
    determinant_inverse = pow(determinant, -1, 26)
    # Compute the adjugate matrix
    adjugate_matrix = np.round(determinant * inverse_matrix) % 26
    # Compute the inverse matrix by multiplying the adjugate matrix by the determinant inverse modulo 26
    inverse_matrix = (adjugate_matrix * determinant_inverse) % 26
    # Perform decryption
    plaintext_matrix = np.dot(ciphertext_matrix, inverse_matrix) % 26
    # Convert numbers to letters
    plaintext = ''.join([chr(int(char) + 65) for sublist in plaintext_matrix.tolist() for char in sublist])
    return plaintext

# Key matrix
key_matrix = np.array([[17, 17, 5], [21, 18, 21], [2, 2, 19]])

# Encrypt the message "PAY"
plaintext = "PAY"
ciphertext = hill_cipher_encrypt(plaintext, key_matrix)
print("Encrypted message:", ciphertext)

# Decrypt the ciphertext to obtain the original plaintext
decrypted_plaintext = hill_cipher_decrypt(ciphertext, key_matrix)
print("Decrypted message:", decrypted_plaintext)
