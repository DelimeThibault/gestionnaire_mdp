"""Création de sites"""


class Sites:
    """Class pour créer/modifier/supprimer un site"""

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        """Afficher le nom"""
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name
