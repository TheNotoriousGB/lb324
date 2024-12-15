from passwortgenerator import *

def main():
    length = int(input("Enter password length: "))
    include_digits = input("Include digits? (y/n): ").lower() == 'y'
    include_special_chars = input("Include special characters? (y/n): ").lower() == 'y'
    print("Generated password:", generate_password(length, include_digits, include_special_chars))

if __name__ == "__main__":
    main()
