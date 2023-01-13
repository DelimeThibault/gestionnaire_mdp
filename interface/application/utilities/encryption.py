"""Sauvegarder, lire et écrire des fichiers cryptés"""
import json
import os.path
from pathlib import Path
from cryptography.fernet import Fernet


class Encryption:
    """Classe pour crypter nos données"""

    # Génère un fichier mykey.key et écris une clé dedans
    @staticmethod
    def key_generation() -> bytes:
        """Génère une clé avec Fernet et la stocke dans un fichier
        PRE : /
        POST :
            key : clé fernet (bytes)
        RAISES :
            FileNotFoundError : fichier non trouvé, le répertoire parent n'existe pas
        """
        key = Fernet.generate_key()
        try:
            if os.path.getsize(Path(r'db/mykey.key')):
                with open(Path(r'db/mykey.key'), 'wb') as file:
                    file.write(key)
                return key
            else:
                raise FileNotFoundError
        except FileNotFoundError:
            return 'dossier db introuvable'


    @staticmethod
    def read_key() -> bytes:
        """Lis la clé Fernet
        PRE : /
        POST :
            key : renvoie la clé sous format 'bytes'
        RAISES : erreur fichier non trouvé
        """
        try:
            if os.path.getsize(Path(r'db/mykey.key')):
                with open(Path(r'db/mykey.key'), 'rb') as file:
                    key = file.read()
                    return key
            else:
                raise FileNotFoundError
        except FileNotFoundError:
            return 'clé introuvable, vérifiez si le dossier ou le fichier existe'

    @staticmethod
    def encryption(key, dict) -> bytes:
        """
        Crypte le dictionnaire en paramètre et le renvoie sur base d'une clé
        PRE :
            key : clé fernet (bytes),
            dict: dictionnaire non crypté (dict)
        POST :
            encrypted: dictionnaire transformé en JSON puis crypté avec la clé en paramètre
        """
        if dict:
            dict_json = json.dumps(dict).encode('utf-8')
            fernet = Fernet(key)
            encrypted = fernet.encrypt(dict_json)
            return encrypted
        else:
            return 'Dictionnaire vide'

    @staticmethod
    def decode(key, encrypted_json) -> dict:
        """
        Décrypte un fichier JSON crypté et le transforme en dictionnaire
        PRE :
            key: clé fernet (bytes),
            encrypted_json: json crypté (dict)
        POST:
            dict_utf8: dictionnaire chargé depuis un fichier JSON décrypté"""
        if encrypted_json:
            fernet = Fernet(key)
            decrypted_json = fernet.decrypt(encrypted_json)
            dict_utf8 = json.loads(decrypted_json)
            return dict_utf8
        else:
            return 'Erreur du format'

    @staticmethod
    def save_json(encrypted_json):
        """
        Opération d'écriture sur le fichier json pour les mdp
        PRE :
            encrypted_json : json crypté (dict)
        POST : / (écrit dans le json les données reçues en PRE)
        RAISES :
            FileNotFoundError : fichier non trouvé
        """
        try:
            if os.path.getsize(Path(r"db")):
                with open(Path(r"db/credentials.json"), 'wb') as file:
                    file.write(encrypted_json)
            else:
                raise FileNotFoundError
        except FileNotFoundError:
            return "ERROR DB NOT FOUND"

    @staticmethod
    def save_signin(encrypted_json):
        """
        Opération d'écriture sur le fichier json pour la connexion
        PRE :
            encrypted_json : json crypté (dict)
        POST : / (écrit dans le json les données reçues en PRE)
        RAISES :
            FileNotFoundError : fichier non trouvé
        """
        try:
            if os.path.getsize(Path(r"db")):
                with open(Path(r"db/signin.json"), 'wb') as file:
                    file.write(encrypted_json)
            else:
                raise FileNotFoundError
        except FileNotFoundError:
            return "ERROR DB NOT FOUND"
