"""Fonctions qui génèrent un mdp, vérifie s'il est fort, s'il est unique,"""
import random

def password_generation():
    """"Génération du mot de passe
    PRE : /
    POST : Renvoi un mot de passe fort qui respecte les critères présents dans le while.
    """
    alph_min = "abcdefghijklmnopqrstuvwxyz"
    alph_maj = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    nombres = "0123456789"
    symboles = r"@#$%&/\?"
    flag_char = False
    flag_number = False
    flag_special = False
    password = ""

    characters = alph_min + alph_maj + nombres + symboles
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


def is_strong(password):
    """Fonction qui permet de voir si le mot de passe est assez fort (possède maj, min,
    nombre, caractère spécial, longueur de 13 caractères)
    PRE : un mot de passe
    POST : Renvoi True si le mdp les critères sont respectées. False si ce n'est pas le cas
    """
    flag_char = False
    flag_number = False
    flag_special = False
    length = len(password)

    if length <= 12:
        return f"Votre mot de passe n'est pas assez long. Il possède {length} caractères"
    for i in password:
        if i.isalpha():
            flag_char = True
        if i.isdigit():
            flag_number = True
        if not i.isalnum():
            flag_special = True
    if flag_char & flag_number & flag_special:
        return True
    return False

def is_unique(password):
    """Fonction qui permet de voir si le mot de passe est utilisé dans le dictionnaire
    PRE : un mot de passe
    POST : renvoi True si le mdp n'est pas dans le dictionnaire, False s'il y est déjà.
    """
    dict_pwd = {}
    if password in dict_pwd:
        return False
    return True
