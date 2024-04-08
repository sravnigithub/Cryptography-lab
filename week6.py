#1.Euclidean Algorithm

def euclidean_algorithm(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def main():
    # Dynamically taking input from the user
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    # Performing Euclidean algorithm
    gcd = euclidean_algorithm(num1, num2)

    print("GCD of", num1, "and", num2, "is:", gcd)

if __name__ == "__main__":
    main()


#2.Extended Euclidean Algorithm

def extended_euclidean_algorithm(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x1, y1 = extended_euclidean_algorithm(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y

def main():
    # Dynamically taking input from the user
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    # Performing Extended Euclidean algorithm
    gcd, x, y = extended_euclidean_algorithm(num1, num2)

    print("GCD of", num1, "and", num2, "is:", gcd)
    print("Coefficients (x, y) such that ax + by = gcd are:", x, y)

if __name__ == "__main__":
    main()

#3.Simple RSA Algorithm with smallnumbers

import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def multiplicative_inverse(e, phi):
    d = 0
    x1, x2 = 0, 1
    y1, y2 = 1, 0
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi // e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2 - temp1 * x1
        y = y2 - temp1 * y1

        x2 = x1
        x1 = x
        y2 = y1
        y1 = y

    if temp_phi == 1:
        d = y2 + phi

    return d

def generate_prime():
    while True:
        num = random.randint(50, 100)
        if is_prime(num):
            return num

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_keypair():
    p = generate_prime()
    q = generate_prime()
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randrange(1, phi)
    gcd_value = gcd(e, phi)
    while gcd_value != 1:
        e = random.randrange(1, phi)
        gcd_value = gcd(e, phi)
    d = multiplicative_inverse(e, phi)
    return ((e, n), (d, n))

def encrypt(public_key, plaintext):
    e, n = public_key
    cipher = [pow(ord(char), e, n) for char in plaintext]
    return cipher

def decrypt(private_key, ciphertext):
    d, n = private_key
    plain = [chr(pow(char, d, n)) for char in ciphertext]
    return ''.join(plain)

if __name__ == '__main__':
    public_key, private_key = generate_keypair()
    print("Public Key:", public_key)
    print("Private Key:", private_key)

    message = input("Enter your message: ")
    print("Original Message:", message)

    encrypted_msg = encrypt(public_key, message)
    print("Encrypted Message:", encrypted_msg)

    decrypted_msg = decrypt(private_key, encrypted_msg)
    print("Decrypted Message:", decrypted_msg)


