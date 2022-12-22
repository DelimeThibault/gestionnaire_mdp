
from interface.application import application
from interface.application.sites.credentials import Credentials
import unittest
import json

class TestAddCredentials(unittest.TestCase):

    def test_valid_input(self):
        # Test avec une entrée valide
        new_cred = Credentials('lulu', 'password123')
        result = application.add_credentials('gmail', new_cred.username, new_cred.password)
        self.assertEqual(result, {'gmail': {'lulu': 'password123'}})

    def test_empty_site(self):
        # Test avec un nom de site vide
        new_cred = Credentials('lulu', 'password123')
        result = application.add_credentials('', new_cred.username, new_cred.password)
        self.assertEqual(result, {'':{'lulu': 'password123'}})

    def test_empty_username(self):
        # Test avec un nom d'utilisateur vide
        new_cred = Credentials('', 'password123')
        result = application.add_credentials('gmail', new_cred.username, new_cred.password)
        self.assertEqual(result, {'gmail':{'': 'password123'}})

    def test_empty_password(self):
        # Test avec un mot de passe vide
        new_cred = Credentials('lulu', '')
        result = application.add_credentials('gmail', new_cred.username, new_cred.password)
        self.assertNotEqual(result, {'gmail':{'lulu':''}})

if __name__ == '__main__':
    unittest.main()

