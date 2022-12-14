"""Création du nom d'utilisateur et mdp avec vérification de celui-ci"""
from packages.sites.sites import Sites
from packages.utilities.password_function import is_strong, is_unique, password_generation
class Credentials:
    """Création du nom d'utilisateur et mdp avec vérification de celui-ci"""
    def __init__(self, user_name, password):
        self.__user_name = user_name
        self.__password = password

    @property
    def user_name(self):
        """Afficher le nom d'utilisateur"""
        return self.__user_name

    @property
    def password(self):
        """Afficher le mot de passe"""
        return self.__password

    @user_name.setter
    def user_name(self, user_name):
        self.user_name = user_name

    @password.setter
    def password(self, password):
        self.password = password

    def good_password(self):
        """Vérification si le mot de passe est correct
        PRE : un mot de passe doit être défini
        POST : Renvoi True si le mdp est unique et fort
        """
        assert self.__password != "", "Il est nécessaire qu'un mot de passe soit défini"
        if not is_strong(self.__password):
            return "Votre mot de passe n'est pas assez fort"
        if not is_unique(self.__password):
            return "Votre mot de passe n'est pas unique "
        return True

test = {}
tmp_site = Sites("Twitter", "www.twitter.com")
tmp_user_mdp = Credentials("user_name_test", password_generation())
test[tmp_site.name] = {tmp_user_mdp.user_name: tmp_user_mdp.password}
print(test)
