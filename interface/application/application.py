"""Module parent utilisant les objets Credentials et les connexions MongoDB"""
from .sites.sites import Sites
from .sites.credentials import Credentials

# Sites = sites.Sites
# Credentials = credentials.Credentials


class Application:
    """Classe parent permettant la création/modification/suppression d'objets Credentials"""

    def add_credentials(self, site, pseudo, password, url="undefined"):
        """
        PRE : reçoit le nom du site (String), le pseudo (String) et le mot de passe (String) ainsi que l'url (non-obligatoire)
        POST : Créé une entrée dans la base de données avec les informations
        """
        new_site = Sites(site, url)
        new_cred = Credentials(pseudo, password)
        obj = {}
        obj[new_site.name] = {new_cred.username: new_cred.password}
        print(obj)

    def modify_credentials(self):
        """
        PRE : reçoit le nom du site (String) et le pseudo (String)
        POST : update la db avec ces informations
        """
        pass
