"""Création du nom d'utilisateur et mdp avec vérification de celui-ci"""
import random
import string


class Credentials:
    """Création du nom d'utilisateur et mdp avec vérification de celui-ci"""

    def __init__(self, username: str, password: str = None):
        self.__username = username
        if password:
            self.__password = password
        else:
            self.__password = self.password_generation()

    @property
    def username(self):
        """Afficher le nom d'utilisateur"""
        return self.__username

    @property
    def password(self):
        """Afficher le mot de passe"""
        return self.__password

    @username.setter
    def username(self, username: str):
        self.username = username

    @password.setter
    def password(self, password: str):
        self.password = password

    @staticmethod
    def password_generation():
        """"Génération du mot de passe
        PRE : /
        POST : Renvoi un mot de passe fort qui respecte les critères présents dans le while.
        """
        characters = string.ascii_letters + string.punctuation + string.digits
        flag_char = False
        flag_number = False
        flag_special = False
        password = ""
        pwd_length = 13

        while not flag_char & flag_number & flag_special:
            password = "".join(random.sample(characters, pwd_length))
            for i in password:
                if i.isalpha():
                    flag_char = True
                if i.isdigit():
                    flag_number = True
                if not i.isalnum():
                    flag_special = True
        return password

    def is_unique(self):
        """Fonction qui permet de voir si le mot de passe est utilisé dans le dictionnaire
        PRE : une chaine de caractères
        POST : renvoi True si le mdp n'est pas dans le dictionnaire, False s'il y est déjà.
        """
        # vérification du type de la variable "password"
        assert isinstance(
            self.password, str), "Veuillez entrer une chaîne de caractères"

        dict_pwd = {}
        if self.password in dict_pwd:
            return False
        return True

    def is_strong(self):
        """Fonction qui permet de voir si le mot de passe est assez fort (possède maj, min,
        nombre, caractère spécial)
        PRE : une chaîne de caractères
        POST : Renvoi True si le mdp les critères sont respectées. False si ce n'est pas le cas
        """
        # vérification du type de la variable "password"
        assert isinstance(
            self.password, str), "Veuillez entrer une chaine de caractères"
        flag_char = False
        flag_number = False
        flag_special = False

        for i in self.password:
            if i.isalpha():
                flag_char = True
            if i.isdigit():
                flag_number = True
            if not i.isalnum():
                flag_special = True
        if flag_char & flag_number & flag_special:
            return True
        return False

    def good_password(self):
        """Vérification si le mot de passe est correct
        PRE : un mot de passe doit être défini
        POST : Renvoie True si le mdp est unique, fort et d'une longueur minimum de 12
        """
        not_secure = ""
        # vérification du type de la variable "password"
        assert isinstance(
            self.password, str), "Veuillez entrer une chaîne de caractères"
        if len(self.password) <= 12:
            not_secure += "Votre mot de passe est trop court, longueur minimum: 12\n"
            return False, not_secure
        if not self.is_strong():
            not_secure += "Votre mot de passe n'est pas assez fort:\n Il faut au moins un caractère alphanumérique, un chiffre et un caractère spécial\n"
            return False, not_secure
        if not self.is_unique():
            not_secure += "Votre mot de passe n'est pas unique"
            return False, not_secure
        return True
