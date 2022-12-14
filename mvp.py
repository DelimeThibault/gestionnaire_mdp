"""MVP """
import cmd


class Credentials:
    """
    Class which contains a dictionary with websites, username and password.
    """

    def __init__(self, dico=None):
        if dico is None:
            dico = {}
        self.__dico = dico

    def update(self, dico):
        """
        Replace 'dict' attribute by the one given in parameter
        Parameter:
            dict: dictionary, required
        """
        if dico:
            self.__dico = dico

    def display_pwd(self):
        """Display every information in Credentials attribute"""
        dict_pwd = self.__dico
        for site in dict_pwd:
            print("nom du site :", site, "\n------------------------")
            for pseudo in dict_pwd[site]:
                password = dict_pwd[site][pseudo]
                print("nom d'utilisateur :", pseudo,
                      "\nmot de passe :", password, "\n")
        return dict_pwd

    def add_logs(self, site, username, password):
        """
        Function to add credentials to our data

        Parameters:
            site: str, required
            username : str, required
            password : str, required
        Returns : None
        """
        if site == "":
            return "Merci d'indiquer le site en premier paramètre de la fonction"
        if site in self.__dico:
            print("existe")
            self.__dico[site][username] = password
        else:
            self.__dico[site] = {
                username: password
            }
        return None

    def __str__(self):
        sentence = ""
        for site in self.__dico:
            sentence = sentence + site + "\n"
        return sentence


class Interaction(cmd.Cmd):
    """
    A class to make a CLI loop with multiple methods
    """
    intro = 'Bienvenue dans le gestionnaire de MDP. Tapez ? pour la liste des commandes.\n'
    prompt = "(MVP) "

    @staticmethod
    def do_init(self):
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

    @staticmethod
    def do_create(self):
        """Permet de créer un nouveau MDP"""
        site = input("nom du site: ")
        username = input("nom d'utilisateur: ")
        password = input("mot de passe: ")
        MVP.add_logs(site, username, password)

    @staticmethod
    def do_display(self):
        """Affiche la liste des MDP"""
        MVP.display_pwd()

    @staticmethod
    def do_exit(self):
        """Ferme le logiciel"""
        return True


if __name__ == "__main__":
    MVP = Credentials()
    Interaction().cmdloop()
