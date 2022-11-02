import random
class Credentials:
    def __init__(self, dict={}):
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

    def __str__(self):
        sentence = ""
        for site in self.__dict:
            sentence = sentence + site + "\n"
        return sentence

dict_cred = {
    "gmail": {"user@gmail.com": "test_mdp_gmail"},
    "Facebook": {"user_facebook": "test_mdp_facebook"},
    "twitter": {
        "user_twitter": "test_mdp_twitter", 
        "toto": "test_deuxieme_mdp"
    }
}

if __name__ == "__main__":
    MVP = Credentials(dict_cred)
    MVP.display_pwd()
    MVP.add_logs("twitter","test fonction", "motdepasse")
    MVP.display_pwd()