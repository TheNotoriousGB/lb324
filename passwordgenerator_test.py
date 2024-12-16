import unittest
import string
import random
from passwordgenerator import \
    generate_password


class TestPasswordGenerator(unittest.TestCase):

    def test_generate_password_length(self):
        # Test, ob das generierte Passwort die richtige Länge hat
        length = 12
        password = generate_password(length)
        self.assertEqual(len(password), length, f"Password length should be {length}")

    def test_generate_password_default_characters(self):
        # Test, ob das Passwort nur aus Buchstaben besteht (wenn keine Sonderzeichen oder Zahlen hinzugefügt werden)
        length = 8
        password = generate_password(length)
        for char in password:
            self.assertTrue(char in string.ascii_letters, "Password should contain only letters.")

    def test_generate_password_with_digits(self):
        # Test, ob das Passwort auch Zahlen enthält, wenn das Flag für Zahlen gesetzt ist
        length = 10
        password = generate_password(length, include_digits=True)
        self.assertTrue(any(char.isdigit() for char in password), "Password should contain digits.")

    def test_generate_password_with_special_characters(self):
        # Test, ob das Passwort Sonderzeichen enthält, wenn das Flag für Sonderzeichen gesetzt ist
        length = 12
        password = generate_password(length, include_special_chars=True)
        special_characters = string.punctuation
        self.assertTrue(any(char in special_characters for char in password),
                        "Password should contain special characters.")

    def test_generate_password_with_digits_and_special_chars(self):
        # Test, ob das Passwort sowohl Zahlen als auch Sonderzeichen enthält, wenn beide Flags gesetzt sind
        length = 14
        password = generate_password(length, include_digits=True, include_special_chars=True)
        self.assertTrue(any(char.isdigit() for char in password), "Password should contain digits.")
        self.assertTrue(any(char in string.punctuation for char in password),
                        "Password should contain special characters.")

    def test_generate_password_no_special_characters(self):
        # Test, ob kein Sonderzeichen vorhanden ist, wenn das Flag auf False gesetzt ist
        length = 10
        password = generate_password(length, include_special_chars=False)
        self.assertFalse(any(char in string.punctuation for char in password),
                         "Password should not contain special characters.")

    def test_generate_password_no_digits(self):
        # Test, ob keine Zahlen vorhanden sind, wenn das Flag auf False gesetzt ist
        length = 10
        password = generate_password(length, include_digits=False)
        self.assertFalse(any(char.isdigit() for char in password), "Password should not contain digits.")


if __name__ == '__main__':
    unittest.main()
