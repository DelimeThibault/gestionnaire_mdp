"""Création de sites"""

class Sites:
    """Class pour créer/modifier/supprimer une note"""
    def __init__(self, name, url):
        self.name = name
        self.url = url

    @property
    def name(self):
        """Afficher le nom"""
        return self.name

    @property
    def url(self):
        """Afficher l'URL"""
        return self.url

    @name.setter
    def name(self, name):
        self.name = name

    @url.setter
    def url(self, url):
        self.url = url

    def __del__(self):
        print("site supprimé")
