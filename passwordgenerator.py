import random
import string


def generate_password(length, include_digits=True, include_special_chars=True):
    # Basiszeichen (Buchstaben)
    characters = string.ascii_letters

    # Wenn Ziffern eingeschlossen werden sollen, füge sie hinzu
    if include_digits:
        characters += string.digits

    # Wenn Sonderzeichen eingeschlossen werden sollen, füge sie hinzu
    if include_special_chars:
        characters += string.punctuation

    # Generiere das Passwort durch zufällige Auswahl von Zeichen
    password = "".join(random.choices(characters, k=length))

    return password
