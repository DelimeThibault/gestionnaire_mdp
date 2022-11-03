import random, cmd, sys
class Credentials:
    def __init__(self, dict=None):
        if dict is None:
            dict = {}
        self.__dict = dict

    def update(self, dict):
        if dict:
            self.__dict = dict

    def display_pwd(self):
        dict_pwd = self.__dict
        for site in dict_pwd:
            print("nom du site :", site, "\n------------------------")
            for pseudo in dict_pwd[site]:
                password = dict_pwd[site][pseudo]
                print("nom d'utilisateur :", pseudo, "\nmot de passe :", password, "\n")
        return dict_pwd


    def add_logs(self, site="", username="", password=""):
        if site == "":
            return "Merci d'indiquer le site en premier paramètre de la fonction"
        if site in self.__dict:
            print("existe")
            self.__dict[site][username] = password
        else:
            self.__dict[site] = {
                username: password
            }

    def __str__(self):
        sentence = ""
        for site in self.__dict:
            sentence = sentence + site + "\n"
        return sentence

class Interaction(cmd.Cmd):
    intro = 'Bienvenue dans le gestionnaire de MDP. Tapez ? pour la liste des commandes.\n'
    prompt = "(MVP) "

    def do_init(self, line):
        """Donne des valeurs tests par défaut"""
        dict_cred = {
            "gmail": {"user@gmail.com": "test_mdp_gmail"},
            "Facebook": {"user_facebook": "test_mdp_facebook"},
            "twitter": {
                "user_twitter": "test_mdp_twitter", 
                "toto": "test_deuxieme_mdp"
            }
        }
        MVP.update(dict_cred)

    def do_create(self, arg):
        """Permet de créer un nouveau MDP"""
        site = input("nom du site: ")
        username = input("nom d'utilisateur: ")
        password = input("mot de passe: ")
        MVP.add_logs(site, username, password)
    
    def do_display(self, line):
        """Affiche la liste des MDP"""
        MVP.display_pwd()

    def do_EXIT(self, line):
        """Ferme le logiciel"""
        return True

if __name__ == "__main__":
    MVP = Credentials()
    Interaction().cmdloop()