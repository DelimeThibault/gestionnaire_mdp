"""Classe Application gérant les autres objets nécessaires aux mots de passe"""
from dotenv import load_dotenv
import os
import pymongo
from pymongo import MongoClient

load_dotenv()
cluster = MongoClient(os.getenv("MONGO"))

db = cluster["DEV2"]
collection = db["credentials"]

# collection.insert_one({
#     "gmail": {"user@gmail.com": "test_mdp_gmail"},
#     "Facebook": {"user_facebook": "test_mdp_facebook"},
#     "twitter": {
#         "user_twitter": "test_mdp_twitter",
#         "toto": "test_deuxieme_mdp"
#     }
# })

results = collection.find()
for document in results:
    print(document)

# class Application:
#     """Classe parent permettant la création/modification/suppression d'objets Credentials"""

#     # def __init__(self, name):
#     #     self.__name = name

#     def add_site(self, name, url="undefined"):
#         pass
