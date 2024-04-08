from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2

def encrypt(plaintext, password):
    salt = get_random_bytes(16)
    key = PBKDF2(password, salt, dkLen=32)
    cipher = AES.new(key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(plaintext)
    return (salt, ciphertext, cipher.nonce, tag)

def decrypt(salt, ciphertext, nonce, tag, password):
    key = PBKDF2(password, salt, dkLen=32)
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)
    return plaintext

def main():
    password = input("Enter password: ").encode('utf-8')
    plaintext = input("Enter plaintext: ").encode('utf-8')

    salt, ciphertext, nonce, tag = encrypt(plaintext, password)
    decrypted_text = decrypt(salt, ciphertext, nonce, tag, password)

    print("Plaintext:", plaintext.decode('utf-8'))
    print("Decrypted Text:", decrypted_text.decode('utf-8'))

if __name__ == "__main__":
    main()
