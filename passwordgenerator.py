import random
import string

def generate_password(length, include_digits=True, include_special_chars=True):
    characters = string.ascii_letters
    if include_digits:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password