import random
# fonction qui créée un mdp
def generateur_mdp():
    alph_min = "abcdefghijklmnopqrstuvwxyz"
    alph_maj = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    nombres = "0123456789"
    symboles = "@#$%&/\?"
    cpt_lettre = False
    cpt_chiffre = False
    cpt_car = False
    mdp = ""

    caractere = alph_min + alph_maj + nombres + symboles
    taille_mdp = 13

    while not (cpt_chiffre & cpt_lettre & cpt_car):
        mdp = "".join(random.sample(caractere, taille_mdp))
        for i in mdp:
            if i.isalpha():
                cpt_lettre = True
            if i.isdigit():
                cpt_chiffre = True
            if not i.isalnum():
                cpt_car = True

    return "Votre nouveau mot de passe est : " + mdp + "\n"

def afficher_mdp():
    dict_mdp = {"gmail": {"user@gmail.com": "test_mdp_gmail"},
                 "Facebook": {"user_facebook": "test_mdp_facebook"},
                 "twitter": {"user_twitter": "test_mdp_twitter", "toto": "test_deuxieme_mdp"}}
    for site in dict_mdp:
        for log in dict_mdp[site]:
            print("nom du site :", site, "\nnom d'utilisateur :", log, "\nmot de passe :", dict_mdp[site][log], "\n")
    return dict_mdp

if __name__ == "__main__":
    print(generateur_mdp())
    afficher_mdp()
