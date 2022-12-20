"""Sauvegarder, lire et écrire des fichiers cryptés"""
import json
from pathlib import Path
from cryptography.fernet import Fernet


class Encryption:
    """Classe pour crypter nos données"""

    # Génère un fichier mykey.key et écris une clé dedans
    @staticmethod
    def key_generation() -> str:
        key = Fernet.generate_key()
        with open(Path(r'db/mykey.key'), 'wb') as file:
            file.write(key)
        return key

    @staticmethod
    def read_key() -> str:
        with open(Path(r'db/mykey.key'), 'rb') as file:
            key = file.read()
            return key

    @staticmethod
    def encryption(key, dict) -> dict:
        dict_json = json.dumps(dict).encode('utf-8')
        fernet = Fernet(key)
        encrypted = fernet.encrypt(dict_json)
        return encrypted

    @staticmethod
    def decode(key, encrypted_json) -> dict:
        fernet = Fernet(key)
        decrypted_json = fernet.decrypt(encrypted_json)
        dict_utf8 = json.loads(decrypted_json)
        return dict_utf8

    @staticmethod
    def save_json(encrypted_json):
        try:
            with open(Path(r"db/credentials.json"), 'wb') as file:
                file.write(encrypted_json)
        except FileNotFoundError:
            return "ERROR DB NOT FOUND"

    @staticmethod
    def save_signin(encrypted_json):
        try:
            with open(Path(r"db/signin.json"), 'wb') as file:
                file.write(encrypted_json)
        except FileNotFoundError:
            return "ERROR DB NOT FOUND"
