from interface.application.utilities.encryption import Encryption
import unittest
import os
from pathlib import Path

test_dir = Path(r'db')
keypath = Path(r'db/mykey.key')
sign_file = Path(r'db/signin.json')
cred_file = Path(r'db/credentials.json')
icon = Path(r"interface/lock.ico")

is_key = os.path.isfile(keypath)

json = {
    'test': 'je suis un test',
    'test2': 'je suis le 2e élément'
}
# Création du répertoire si absent
if not os.path.isdir(test_dir):
    os.mkdir('db')
class TestEncryption(unittest.TestCase):
    # Classe de test pour la classe "Encryption"
    def test_create_key(self):
        # Test de la génération d'une clé fernet pour chiffrer les données
        # On regarde si le fichier existe déjà
        if is_key:
            # On regarde s'il est vide
            if os.path.getsize(keypath) == 0:
                Encryption.key_generation()
                self.assertGreater(os.path.getsize(keypath), 0)
            else:
                self.assertGreater(os.path.getsize(keypath), 0)
        # Si le fichier n'existe pas, on le génère
        else:
            Encryption.key_generation()
            self.assertGreater(os.path.getsize(keypath), 0)

    def test_read_key(self):
        # Test de la lecture d'un fichier byte
        key = Encryption.read_key()
        self.assertEqual(type(key), bytes)

    def test_encrypt_dict(self):
        # le fichier dict doit se transformer en json chiffré (bytes)
        key = Encryption.read_key()
        empty = {}
        empty_result = Encryption.encryption(key, empty)
        self.assertEqual(empty_result, 'Dictionnaire vide')
        result = Encryption.encryption(key, json)
        self.assertEqual(type(result), bytes)

    def test_decode_dict(self):
        # On transforme un dict en bytes et on le retransforme en dict pour vérifier que notre classe sait déchiffrer
        key = Encryption.read_key()
        encrypted = Encryption.encryption(key, json)
        decoded = Encryption.decode(key, encrypted)
        empty = {}
        empty_decoded = Encryption.decode(key, empty)
        self.assertEqual(type(decoded), dict)
        self.assertEqual(json, decoded)
        self.assertEqual(empty_decoded, 'Erreur du format')

    def test_save_json(self):
        # Test d'écriture disque en format JSON
        key = Encryption.read_key()
        encrypted = Encryption.encryption(key, json)
        Encryption.save_json(encrypted)
        file_size = os.path.getsize(cred_file)
        # Vérification de la taille du fichier (doit être différent de 0)
        self.assertGreater(file_size, 0)
    def test_save_signin(self):
        # Test d'écriture disque en format JSON
        key = Encryption.read_key()
        encrypted = Encryption.encryption(key, json)
        Encryption.save_signin(encrypted)
        file_size = os.path.getsize(sign_file)
        # Vérification de la taille du fichier (doit être différent de 0)
        self.assertGreater(file_size, 0)

if __name__ == "__main__":
    unittest.main()

