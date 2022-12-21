"""Module parent utilisant les objets Credentials et les connexions MongoDB"""
from .sites.credentials import Credentials


def add_credentials(site: str, username: str, password: str):
    """
    PRE : reçoit le nom du site (String), le pseudo (String) et le mot de passe (String)
    ainsi que l'url (non obligatoire)
    POST : Créé une entrée dans la base de données avec les informations
    """

    new_cred = Credentials(username, password)
    obj = {site: {new_cred.username: new_cred.password}}
    return obj
