"""Sauvegarder, lire et écrire des fichiers cryptés"""
import json
from pathlib import Path
from cryptography.fernet import Fernet


class Encryption:
    """Classe pour crypter nos données"""

    # Génère un fichier mykey.key et écris une clé dedans
    @staticmethod
    def key_generation() -> str:
        """Génère une clé avec Fernet et la stocke dans un fichier"""
        key = Fernet.generate_key()
        with open(Path(r'db/mykey.key'), 'wb') as file:
            file.write(key)
        return key

    @staticmethod
    def read_key() -> str:
        """Lis la clé Fernet"""
        with open(Path(r'db/mykey.key'), 'rb') as file:
            key = file.read()
            return key

    @staticmethod
    def encryption(key, dict) -> dict:
        """
        Crypte le dictionnaire en paramètre et le renvoie sur base d'une clé
        PRE :
            key : clé fernet (str),
            dict: dictionnaire non crypté (dict)
        POST :
            encrypted: dictionnaire transformé en JSON puis crypté avec la clé en paramètre
        """
        dict_json = json.dumps(dict).encode('utf-8')
        fernet = Fernet(key)
        encrypted = fernet.encrypt(dict_json)
        return encrypted

    @staticmethod
    def decode(key, encrypted_json) -> dict:
        """
        Décrypte un fichier JSON crypté et le transforme en dictionnaire
        PRE :
            key: clé fernet (str),
            encrypted_json: json crypté (dict)
        POST:
            dict_utf8: dictionnaire chargé depuis un fichier JSON décrypté"""
        fernet = Fernet(key)
        decrypted_json = fernet.decrypt(encrypted_json)
        dict_utf8 = json.loads(decrypted_json)
        return dict_utf8

    @staticmethod
    def save_json(encrypted_json):
        """
        Opération d'écriture sur le fichier json pour les mdp
        """
        try:
            with open(Path(r"db/credentials.json"), 'wb') as file:
                file.write(encrypted_json)
        except FileNotFoundError:
            return "ERROR DB NOT FOUND"

    @staticmethod
    def save_signin(encrypted_json):
        """
        Opération d'écriture sur le fichier json pour la connexion
        """
        try:
            with open(Path(r"db/signin.json"), 'wb') as file:
                file.write(encrypted_json)
        except FileNotFoundError:
            return "ERROR DB NOT FOUND"
