
import unittest
from passwordgenerator import generate_password


import unittest
from passwordgenerator import generate_password


def main():
    length = int(input("Enter password length: "))
    include_digits = input("Include digits? (y/n): ").lower() == "y"
    include_special_chars = input("Include special characters? (y/n): ").lower() == "y"

    result = generate_password(length, include_digits, include_special_chars)

    print("Generated password:", result)


if __name__ == "__main__":
    unittest.main()
    main()
