"""Fonction qui créée un mdp"""
import random

def password_gen():
    """"Génération du mot de passe"""
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
