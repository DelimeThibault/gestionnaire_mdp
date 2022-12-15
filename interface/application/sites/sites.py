"""Création de sites"""

class Sites:
    """Class pour créer/modifier/supprimer un site"""

    def __init__(self, name, url):
        self.__name = name
        self.__url = url

    @property
    def name(self):
        """Afficher le nom"""
        return self.__name

    @property
    def url(self):
        """Afficher l'URL"""
        return self.__url

    @name.setter
    def name(self, name):
        self.__name = name

    @url.setter
    def url(self, url):
        self.__url = url
