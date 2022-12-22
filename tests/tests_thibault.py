"""Fichier qui tests les différentes fonctions et méthodes"""
import unittest
from interface.application.sites.credentials import Credentials


class TestCredentials(unittest.TestCase):
    def test_init(self):
        user_psw = Credentials("user_name", "password")
        self.assertEqual(user_psw.username, "user_name")
        self.assertEqual(user_psw.password, "password")

    def test_password_generetion(self):
        pwd = Credentials.password_generation()
        self.assertNotEqual(pwd, None)
        self.assertEqual(len(pwd), 13)

    def test_is_unique(self):
        test = Credentials("test", "test")
        self.assertTrue(test.is_unique(), True)

    def test_is_strong(self):
        test_true = Credentials("test", "i}u+8t%*{n&\I")
        test_false = Credentials("test_username", "test_mdp")
        self.assertTrue(test_true.is_strong())
        self.assertFalse(test_false.is_strong())

    def test_good_password(self):
        test_true = Credentials("test", "i}u+8t%*{n&\I")
        test_len = Credentials("test_username", "i}u+8")
        test_strong = Credentials("test_username", "2132tested12345")
        self.assertTrue(test_true.good_password())
        # false car la taille n'est pas bonne
        self.assertFalse(test_len.good_password()[0])
        # false car il n'est pas strong (pas de chars spéciaux)
        self.assertFalse(test_strong.good_password()[0])


if __name__ == '__main__':
    unittest.main()
