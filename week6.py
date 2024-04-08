#1.

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


#2.

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


