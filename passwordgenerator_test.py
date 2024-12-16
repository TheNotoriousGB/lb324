import unittest
import string
from passwordgenerator import generate_password  # Importiere den Passwortgenerator


class TestPasswordGenerator(unittest.TestCase):

    def test_generate_password_default_characters(self):
        # Teste die Generierung von Passwörtern nur mit Buchstaben
        password = generate_password(length=8, include_digits=False, include_special_chars=False)

        # Überprüfe, dass das Passwort nur Buchstaben enthält
        self.assertTrue(all(char in string.ascii_letters for char in password), "Password should contain only letters.")

    def test_generate_password_with_digits(self):
        # Teste die Generierung von Passwörtern mit Ziffern
        password = generate_password(length=8, include_digits=True, include_special_chars=False)

        # Überprüfe, dass das Passwort mindestens eine Ziffer enthält
        self.assertTrue(any(char.isdigit() for char in password), "Password should contain digits.")

    def test_generate_password_with_special_chars(self):
        # Teste die Generierung von Passwörtern mit Sonderzeichen
        password = generate_password(length=8, include_digits=False, include_special_chars=True)

        # Überprüfe, dass das Passwort mindestens ein Sonderzeichen enthält
        self.assertTrue(any(char in string.punctuation for char in password),
                        "Password should contain special characters.")

    def test_generate_password_with_all_options(self):
        # Teste die Generierung von Passwörtern mit Buchstaben, Ziffern und Sonderzeichen
        password = generate_password(length=12, include_digits=True, include_special_chars=True)

        # Überprüfe, dass das Passwort Ziffern enthält
        self.assertTrue(any(char.isdigit() for char in password), "Password should contain digits.")

        # Überprüfe, dass das Passwort Sonderzeichen enthält
        self.assertTrue(any(char in string.punctuation for char in password),
                        "Password should contain special characters.")

        # Überprüfe, dass das Passwort Buchstaben enthält
        self.assertTrue(any(char in string.ascii_letters for char in password), "Password should contain letters.")


if __name__ == "__main__":
    unittest.main()
