"""Création de notes"""

class Notes:
    """Class pour créer/modifier/supprimer une note"""
    def __init__(self, title, text):
        self.title = title
        self.text = text

    @property
    def title(self):
        """Afficher le titre"""
        return self.title

    @property
    def text(self):
        """Afficher le texte"""
        return self.text

    @title.setter
    def title(self, title):
        self.title = title

    @text.setter
    def text(self, text):
        self.text = text

    def __del__(self):
        print("note supprimé")
