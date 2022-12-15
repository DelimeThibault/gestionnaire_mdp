"""Module parent utilisant les objets Credentials et les connexions MongoDB"""
import os
from dotenv import load_dotenv
import pymongo
from pymongo import MongoClient
from .sites.sites import Sites
from .sites.credentials import Credentials

# Sites = sites.Sites
# Credentials = credentials.Credentials
load_dotenv()
cluster = MongoClient(os.getenv("MONGO"))

db = cluster["DEV2"]
collection = db["credentials"]

# results = collection.find()
# for document in results:
#     print(document)


class Application:
    """Classe parent permettant la création/modification/suppression d'objets Credentials"""

    # def __init__(self):
    #     self.__entry = {}

    def add_credentials(self, site, pseudo, password, url="undefined"):
        """
        PRE : reçoit le nom du site (String), le pseudo (String) et le mot de passe (String) ainsi que l'url (non-obligatoire)
        POST : Créé une entrée dans la base de données avec les informations
        """
        new_site = Sites(site, url)
        new_cred = Credentials(pseudo, password)
        obj = {}
        obj[new_site.name] += {new_cred.username: new_cred.password}
        print(obj)
        collection.insert_one(obj)

    def modify_credentials(self):
        """
        PRE : reçoit le nom du site (String) et le pseudo (String)
        POST : update la db avec ces informations
        """
        pass
