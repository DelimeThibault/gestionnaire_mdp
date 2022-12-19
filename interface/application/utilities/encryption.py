"""Sauvegarder, lire et écrire des fichiers cryptés"""
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2
import PBKDF2HMAC
import base64


class Encryption:
    def __init__(self) -> None:
        self.key = ""

    def key_generation(self):
        self.key = Fernet.generate_key()
        with open('mykey.key', 'w') as mykey:
            mykey.write(key)
