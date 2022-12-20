"""Module parent utilisant les objets Credentials et les connexions MongoDB"""
from .sites.sites import Sites
from .sites.credentials import Credentials


class Application:
    """Classe parent permettant la création/modification/suppression d'objets Credentials"""

    @staticmethod
    def add_credentials(site: str, username: str, password: str) -> dict:
        """
        PRE : reçoit le nom du site (String), le pseudo (String) et le mot de passe (String) ainsi que l'url (non-obligatoire)
        POST : Créé une entrée dans la base de données avec les informations
        """

        new_cred = Credentials(username, password)
        obj = dict()
        obj[site] = {new_cred.username: new_cred.password}
        return obj

    def modify_credentials(self):
        """
        PRE : reçoit le nom du site (String) et le pseudo (String)
        POST : update la db avec ces informations
        """
        pass
