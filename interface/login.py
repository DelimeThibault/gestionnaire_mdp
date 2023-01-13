"""Interface graphique qui s'occupe d'appeler des méthodes pour les modules et boutons """
from json.decoder import JSONDecodeError
from tkinter import filedialog as fd
import tkinter as tk
from tkinter import messagebox
from pathlib import Path
import os
from .application import application
from .application.utilities.encryption import Encryption

class PasswordManager(tk.Tk):
    """Interface graphique avec Tkinter"""

    def __init__(self):
        tk.Tk.__init__(self)
        # Créer une fenêtre principale
        self.search_entry = None
        self.search_label = None
        self.delete_password_button = None
        self.edit_password_button = None
        self.add_password_button = None
        self.copy_username_button = None
        self.copy_password_button = None
        self.password_list = None
        self.password_list_label = None
        self.search_frame = None
        self.bottom_password_list_frame = None
        self.top_password_list_frame = None
        self.button = None
        self.new_user = None
        self.pwd_entry = None
        self.label_pwd = None
        self.user_entry = None
        self.label_site = None
        self.modify = None
        self.cred_btn = None
        self.listbox_cred = None
        self.username_frame = None
        self.selected_user = None
        self.site_btn = None
        self.listbox_site = None
        self.add_button = None
        self.selected_site = None
        self.change_frame = None
        self.password_list_frame = None
        self.username_entry = None
        self.username_label = None
        self.site_entry = None
        self.site_label = None
        self.add_frame = None
        self.question_button = None
        self.question_frame = None
        self.login_button = None
        self.login_frame = None
        self.signup_button = None
        self.question_entry = None
        self.question_label = None
        self.password_entry = None
        self.password_label = None
        self.signup_frame = None
        self.new_pwd = None
        self.__this_width = 250
        self.__this_height = 150
        self.title("Gestionnaire de mots de passe")
        self.password_database = {}
        self.signin_database = {}
        self.center_window(self.__this_width, self.__this_height)
        self.clipboard = ""
        self.encrypted_key = ''

        keypath = Path(r'db/mykey.key')
        sign_file = Path(r'db/signin.json')
        cred_file = Path(r'db/credentials.json')
        icon = Path(r"interface/lock.ico")

        is_key = os.path.isfile(keypath)

        if is_key:
            if os.path.getsize(keypath) == 0:
                self.encrypted_key = Encryption.key_generation()
            else:
                self.encrypted_key = Encryption.read_key()
        else:
            self.encrypted_key = Encryption.key_generation()

        # Ouvre le fichier contenant le mdp signin
        try:
            with open(sign_file, 'rb') as file:
                encrypted_signin = file.read()
                try:
                    if os.path.getsize(sign_file) != 0:
                        decrypted_data = Encryption.decode(
                            self.encrypted_key, encrypted_signin)
                        self.signin_database = decrypted_data
                        self.show_login_page()
                    else:
                        self.show_signup_page()
                except TypeError:
                    self.signin_database = encrypted_signin

        except FileNotFoundError:
            self.show_signup_page()
        except JSONDecodeError:
            self.show_signup_page()

        # Ouvre le fichier contenant les credentials
        try:
            with open(cred_file, "rb") as file:
                encrypted_data = file.read()
                # convertit le fichier crypté en un dictionnaire utilisable
                try:
                    if os.path.getsize(cred_file) != 0:
                        decrypted_data = Encryption.decode(
                            self.encrypted_key, encrypted_data)
                        self.password_database = decrypted_data
                except TypeError:
                    self.password_database = encrypted_data
        except FileNotFoundError:
            pass
        except JSONDecodeError:
            pass

        # Change l'icône
        try:
            self.iconbitmap(icon)
        except FileNotFoundError:
            print('Fichier introuvable.')
        except IOError:
            print('Erreur IO.')

    def center_window(self, width, height):
        """Méthode qui centre la fenêtre

        PRE : recoit la largeur (int) et la hauteur (int)
        POST : renvoie la fenêtre de manière centrée

        """
        # Center the window
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # For left-align
        left = (screen_width / 2) - (width / 2)

        # For right-align
        top = (screen_height / 2) - (height / 2)

        # For top and bottom
        self.geometry(
            f'{width}x{height}+{int(left)}+{int(top)}')

    def show_signup_page(self):
        """Méthode qui affiche la fenêtre lors de l'inscription"""
        # Créer un cadre pour afficher le formulaire d'inscription et les widgets associés
        self.signup_frame = tk.Frame(self)
        self.signup_frame.pack()

        # Créer une étiquette et un champ de saisie pour le mot de passe
        self.password_label = tk.Label(self.signup_frame, text="Mot de passe:")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.signup_frame, show="*", width=30)
        self.password_entry.pack()

        # Créer une étiquette et un champ de saisie pour la question personnelle
        self.question_label = tk.Label(
            self.signup_frame, text="Question personnelle: \n Ou êtes-vous né?")
        self.question_label.pack()
        self.question_entry = tk.Entry(self.signup_frame, width=30)
        self.question_entry.pack()

        # Créer un bouton pour s'inscrire
        self.signup_button = tk.Button(
            self.signup_frame, text="S'inscrire", command=self.signup)
        self.signup_button.pack()

    def signup(self):
        """Méthode qui créer l'inscription"""
        # Récupérer le mot de passe et la question personnelle entrés par l'utilisateur
        password = self.password_entry.get()
        question = self.question_entry.get()

        # Vérifier si le mot de passe et la question personnelle sont valides
        # (par exemple, s'assurer qu'ils ne sont pas vides)
        if password == "" or question == "":
            messagebox.showerror(
                "Erreur", "Mot de passe et question personnelle sont obligatoires")
            return

        # Enregistrer le mot de passe et la question personnelle dans la base de données
        self.signin_database["password"] = password
        self.signin_database["question"] = question

        encrypted_sign = Encryption.encryption(
            self.encrypted_key, self.signin_database)
        Encryption.save_signin(encrypted_sign)

        # Afficher un message de confirmation et passer à la page de login
        messagebox.showinfo("Succès", "Inscription réussie!")
        self.show_login_page()
        self.signup_frame.destroy()

    def show_login_page(self):
        """Méthode qui affiche la page de connexion"""
        # Créer un cadre pour afficher le formulaire de login
        self.login_frame = tk.Frame(self)
        self.center_window(340, 90)
        self.login_frame.pack()

        # Créer une étiquette et un champ de saisie pour le mot de passe
        self.password_label = tk.Label(
            self.login_frame, text="Mot de passe:\n "
                                   "(Si vous vous ne souvenez pas de votre mot de passe, tapez o.)")
        self.password_label = tk.Label(
            self.login_frame, text="Mot de passe:\n "
                                   "(Si vous vous ne souvenez pas de votre mot de passe, tapez o.)")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.login_frame, show="*", width=30)
        self.password_entry.pack()

        # Créer un bouton pour se connecter
        self.login_button = tk.Button(
            self.login_frame, text="Se connecter", command=self.login)
        self.login_button.pack()

    def show_question_page(self):
        """Méthode qui affiche la page où l'on pose la question si on oublie son mdp"""
        # détruire la page de login
        self.login_frame.destroy()
        # Créer un cadre pour afficher le formulaire de question
        self.question_frame = tk.Frame(self)
        self.center_window(340, 90)
        self.question_frame.pack()

        # Créer une étiquette et un champ de saisie pour la question
        self.question_label = tk.Label(
            self.question_frame, text="Ou êtes-vous né?")
        self.question_label.pack()
        self.question_entry = tk.Entry(self.question_frame, show="*", width=30)
        self.question_entry.pack()

        # Créer un bouton pour se connecter
        self.question_button = tk.Button(
            self.question_frame, text="Se connecter", command=self.question)
        self.question_button.pack()

    def login(self):
        """Méthode qui permet de se connecter à l'application"""
        # Récupérer le mot de passe entré par l'utilisateur
        password = self.password_entry.get()

        # Vérifier si le mot de passe est correct
        if password == self.signin_database["password"]:
            # Si le mot de passe est correct, afficher la page principale
            self.show_main_page()
        elif password == "o":
            self.show_question_page()
        else:
            # Si le mot de passe est incorrect, afficher un message d'erreur
            messagebox.showerror("Erreur", "Mot de passe incorrect")

    def question(self):
        """Méthode qui permet de vérifier si la réponse à la question posée est correct"""
        # Récupérer la réponse a la question personnelle entrée par l'utilisateur
        question = self.question_entry.get()
        # Vérifier si la réponse a la question personnelle est correct
        if question == self.signin_database["question"]:
            # Si la réponse a la question personnelle est correcte, afficher la page principale
            self.show_main_page()
            self.question_frame.destroy()
        else:
            # Si la réponse a la question personnelle est incorrecte, afficher un message d'erreur
            messagebox.showerror("Erreur", "Réponse a la question incorrecte")

    def add_info(self):
        """Méthode pour ajouter un nouveau mot de passe via une interface supplémentaire"""
        global my_user
        # Créer un cadre pour ajouter les infos
        self.add_frame = tk.Toplevel(self)
        self.add_frame.title("Ajouter un mot de passe")
        # self.add_frame.pack()

        # Créer une étiquette et un champ de saisie pour le mot de passe
        self.site_label = tk.Label(self.add_frame, text="Site:")
        self.site_label.pack()
        my_site = tk.StringVar(self.add_frame)
        self.site_entry = tk.Entry(
            self.add_frame, width=30, textvariable=my_site)
        self.site_entry.pack()
        self.username_label = tk.Label(
            self.add_frame, text="Nom d'utilisateur:")
        self.username_label.pack()
        my_user = tk.StringVar(self.add_frame)
        self.username_entry = tk.Entry(
            self.add_frame, width=30, textvariable=my_user)
        self.username_entry.pack()
        self.password_label = tk.Label(
            self.add_frame, text="Mot de passe: \n "
                                 "(si vous n'en entrez pas, "
                                 "un mot de passe fort sera automatiquement créé)")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.add_frame, show="*", width=30)
        self.password_entry.pack()
        self.password_list_frame = tk.Frame()

        self.password_list_frame.pack()

        # Créer un bouton pour ajouter
        self.add_button = tk.Button(self.add_frame, text="Ajouter", state="disabled",
                                    command=lambda: check_password(self.password_entry.get()))
        self.add_button.pack()

        def check_password(pwd):
            obj = application.Credentials(self.site_entry.get(), pwd)
            (validation, msg_error) = obj.good_password()
            if validation:
                self.add_password(self.site_entry.get().upper(),
                                  self.username_entry.get(), pwd)
            if not validation:
                messagebox.showinfo(
                    'Attention', msg_error, icon=messagebox.WARNING)
                self.add_password(self.site_entry.get().upper(),
                                  self.username_entry.get(), pwd)

        def update(*args):
            if args == 99:
                print("args est égal à 99")
            if len(my_site.get()) == 0 or len(my_user.get()) == 0:
                self.add_button.config(state="disabled")
            else:
                self.add_button.config(state="normal")
        my_user.trace('w', update)
        my_site.trace('w', update)

    def change_password(self, param):
        """
        Méthode pour changer un username ou mot de passe via une interface
        Sélection du site où il faut faire la modification
        """
        self.change_frame = tk.Toplevel(self)
        self.change_frame.geometry("230x200")
        self.eval(f'tk::PlaceWindow {str(self.change_frame)} center')
        if param == "edit":
            self.change_frame.title("Modifier un mot de passe")
        elif param == "delete":
            self.change_frame.title("Supprimer un mot de passe")
        self.selected_site = ""
        self.listbox_site = tk.Listbox(self.change_frame)
        self.listbox_site.pack()
        self.listbox_site.bind('<<ListboxSelect>>', self.change_site)
        for site in self.password_database:
            self.listbox_site.insert(tk.END, site)

        if param == "edit":
            self.site_btn = tk.Button(
                self.change_frame, state="disabled",
                text="Suivant", command=lambda: self.select_username("edit"))
        elif param == "delete":
            self.site_btn = tk.Button(
                self.change_frame, state="disabled",
                text="Suivant", command=lambda: self.select_username("delete"))
        self.site_btn.pack()

    def change_site(self, evt):
        """Stocke la valeur sélectionnée dans listBox dans un attribut self.selected_site"""
        w = evt.widget
        index = int(w.curselection()[0])
        value = w.get(index)
        if value != "":
            self.selected_site = value
            self.site_btn.config(state="normal")

    def change_user(self, evt):
        """Stocke la valeur sélectionnée dans listBox dans un attribut self.selected_user"""
        w = evt.widget
        index = int(w.curselection()[0])
        value = w.get(index)
        if value != "":
            self.selected_user = value
            self.cred_btn.config(state="normal")

    def select_username(self, param):
        """Interface de sélection d'utilisateur dans la base de données"""
        self.change_frame.destroy()
        self.username_frame = tk.Toplevel(self)
        self.username_frame.geometry("230x200")
        self.eval(f'tk::PlaceWindow {str(self.username_frame)} center')
        if param == "edit":
            self.username_frame.title("Modifier un mot de passe")
        elif param == "delete":
            self.username_frame.title("Supprimer un mot de passe")
        self.selected_user = ""
        self.listbox_cred = tk.Listbox(self.username_frame)
        self.listbox_cred.pack()
        self.listbox_cred.bind('<<ListboxSelect>>', self.change_user)
        for username in self.password_database[self.selected_site]:
            self.listbox_cred.insert(
                tk.END, username)
        if param == "edit":
            self.cred_btn = tk.Button(
                self.username_frame, state="disabled",
                text="Modifier", command=lambda: self.modify_credentials("edit"))
        elif param == "delete":
            self.cred_btn = tk.Button(
                self.username_frame, state="disabled",
                text="Supprimer", command=lambda: self.modify_credentials("delete"))
        self.cred_btn.pack()

    def modify_credentials(self, param):
        """Interface pour entrer le nouveau nom et mot de passe"""
        global my_user, my_pwd
        self.username_frame.destroy()
        if param == "edit":
            self.modify = tk.Toplevel(self)
            self.modify.geometry("410x160")
            self.eval(f'tk::PlaceWindow {str(self.modify)} center')
            self.modify.title('Modifier informations')
            my_user = tk.StringVar(self.modify)
            my_pwd = tk.StringVar(self.modify)
            self.label_site = tk.Label(
                self.modify, text="Nouveau nom d'utilisateur "
                                  "(n'écrivez rien si vous voulez le conserver)")
            self.label_site.pack()
            self.user_entry = tk.Entry(self.modify, textvariable=my_user)
            self.user_entry.pack()
            self.label_pwd = tk.Label(
                self.modify, text="Nouveau mot de passe \n "
                                  "(n'écrivez rien si vous voulez le conserver,\n "
                                  "tapez 'g' pour créer un nouveau mot de passe fort)")
            self.label_pwd.pack()
            self.pwd_entry = tk.Entry(self.modify, textvariable=my_pwd)
            self.pwd_entry.pack()
            self.new_user = self.selected_user
            self.new_pwd = ''

            # Bouton pour modifier
            self.button = tk.Button(
                self.modify, text="Mettre à jour", command=self.update_credentials)
            self.button.pack()
        elif param == "delete":
            answer = messagebox.askokcancel(
                title="Suppression d'utilisateur et mot de passe",
                message="Voulez-vous vraiment supprimer: " +
                self.selected_user+" de "+self.selected_site+" ?",
                icon=messagebox.WARNING)
            if answer:
                del self.password_database[self.selected_site][self.selected_user]
                if not self.password_database[self.selected_site]:
                    del self.password_database[self.selected_site]
                self.update_list()
                encrypted_json = Encryption.encryption(
                    self.encrypted_key, self.password_database)
                Encryption.save_json(encrypted_json)

        def update(*args):
            if args == 99:
                print("args est égal à 99")
            if len(my_user.get()) == 0:
                self.new_user = self.selected_user
                if my_pwd.get() == "g":
                    self.new_pwd = application.Credentials.password_generation()
                else:
                    self.new_pwd = my_pwd.get()
            elif len(my_user.get()) > 0:
                self.new_user = my_user.get()
                if my_pwd.get() == "g":
                    self.new_pwd = application.Credentials.password_generation()
                else:
                    self.new_pwd = my_pwd.get()
                del self.password_database[self.selected_site][self.selected_user]
        my_user.trace('w', update)
        my_pwd.trace('w', update)

    def update_list(self, arg="original", copy=None):
        """Méthode qui rafraichit l'affichage sur l'interface principale"""
        if arg == "original":
            self.sort_password()
            self.password_list.delete(0, "end")
            for site, credentials in self.password_database.items():
                self.password_list.insert(tk.END, f" {site}:\n")
                for username, password in credentials.items():
                    self.password_list.insert(tk.END,
                                              f" \t \t \t \t \t{username}, {password}\n")
        elif arg == "copy":
            self.sort_password()
            self.password_list.delete(0, "end")
            for site, credentials in copy.items():
                self.password_list.insert(tk.END, f" {site}:\n")
                for username, password in credentials.items():
                    self.password_list.insert(tk.END,
                                              f" \t \t \t \t \t{username}, {password}\n")

    def show_main_page(self):
        """Page principale qui redirige vers les opérations CRUD (boutons)"""
        # Détruire la page de login et/ou question
        self.login_frame.destroy()
        # Créer un cadre pour afficher la liste des mots de passe enregistrés et les widgets associés
        self.password_list_frame = tk.Frame()
        self.password_list_frame.pack()
        self.top_password_list_frame = tk.Frame()
        self.top_password_list_frame.pack(side="top")
        self.bottom_password_list_frame = tk.Frame()
        self.bottom_password_list_frame.pack(side="top")
        self.search_frame = tk.Frame()
        self.search_frame.pack(side="top")
        self.center_window(450, 350)
        self.password_list_label = tk.Label(
            self.password_list_frame, text="Mots de passe enregistrés:")
        self.password_list_label.pack()
        self.password_list = tk.Listbox(
            self.password_list_frame, height=15, width=60)
        self.password_list.pack()
        self.password_list.bind("<<ListboxSelect>>", self.selected_value)

        # Mettre à jour la liste des mots de passe enregistrés
        self.update_list()

        # Créer un bouton pour copier le mot de passe sélectionné dans le presse-papiers
        self.copy_password_button = tk.Button(
            self.top_password_list_frame,
            text="Copier le mot de passe", command=lambda: self.copy_clipboard("password"))
        self.copy_password_button.pack(side="left")

        # Créer un bouton pour copier le mot de passe sélectionné dans le presse-papiers
        self.copy_username_button = tk.Button(
            self.top_password_list_frame,
            text="Copier le nom d'utilisateur", command=lambda: self.copy_clipboard("username"))
        self.copy_username_button.pack(side="left")

        # Créer un bouton pour ajouter un nouveau mot de passe
        self.add_password_button = tk.Button(
            self.bottom_password_list_frame,
            text="Ajouter un mot de passe", command=self.add_info)
        self.add_password_button.pack(side="left")

        # Créer un bouton pour modifier le mot de passe sélectionné
        self.edit_password_button = tk.Button(
            self.bottom_password_list_frame,
            text="Modifier le mot de passe", command=lambda: self.change_password("edit"))
        self.edit_password_button.pack(side="left")

        # Créer un bouton pour supprimer le mot de passe sélectionné
        self.delete_password_button = tk.Button(
            self.bottom_password_list_frame,
            text="Supprimer le mot de passe", command=lambda: self.change_password("delete"))
        self.delete_password_button.pack(side="left")

        search = tk.StringVar(self.search_frame)
        self.search_label = tk.Label(
            self.search_frame, text="Rechercher un mot de passe :")
        self.search_label.pack(side="left")
        self.search_entry = tk.Entry(self.search_frame, textvariable=search)
        self.search_entry.pack(side="left")

        def search_site(*args):
            """Cette fonction recherche un site entré en paramètre dans la base de donnée
            PRE : /
            POST : Renvoi une string contenant le nom du site, le nom d'utilisateur et le mdp.
            """
            if args == 99:
                print("args est égal à 99")
            copy_database = {}
            site = search.get().upper()
            if len(site):
                for i in self.password_database:
                    if site in i:
                        copy_database[i] = self.password_database[i]
                self.update_list("copy", copy_database)
            else:
                self.update_list()
        search.trace("w", search_site)

    @staticmethod
    def select_file():
        """Permet de sélectionner un fichier s'il n'a pas été trouvé"""
        filetypes = (
            ('json files', '*.json'),
            ('All files', '*.*')
        )

        fd.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes)

    def add_password(self, site, username, password):
        """Ajoute un mot de passe dans le fichier si le couple site/username n'existe pas encore"""
        new_pwd = application.add_credentials(
            site, username, password)
        key = next(iter(new_pwd))
        user = next(iter(new_pwd[key]))
        infos = new_pwd[key]

        if key in self.password_database.keys():
            if user in self.password_database[key]:
                return "Cet utilisateur existe déjà"
            self.password_database[key].update(infos)
        else:
            self.password_database[key] = infos
        # Ouvre le fichier contenant les mdp
        encrypted_json = Encryption.encryption(
            self.encrypted_key, self.password_database)
        Encryption.save_json(encrypted_json)

        self.update_list()
        self.add_frame.destroy()
        return None

    def sort_password(self):
        """Trie notre dictionnaire par ordre alphabétique
        PRE : /
        POST : Renvoi le dictionnaire trié par ordre alphabétique.
        """
        dict_sort = dict(sorted(self.password_database.items())).copy()
        for i in dict_sort:
            dict_sort[i] = dict(sorted(dict_sort[i].items()))

        self.password_database = dict_sort

    def update_credentials(self):
        """Ecriture dans la db du changement de credentials"""
        site = self.selected_site
        user = self.new_user
        if self.new_pwd == "":
            self.new_pwd = self.password_database[site][user]
        self.password_database[site][user] = self.new_pwd
        self.update_list()
        encrypted_json = Encryption.encryption(
            self.encrypted_key, self.password_database)
        Encryption.save_json(encrypted_json)

        self.modify.destroy()

    def selected_value(self, evt):
        """Obtient la valeur de la phrase sélectionnée dans la listBox principale"""
        w = evt.widget
        index = int(w.curselection()[0])
        value = w.get(index)
        if value != "":
            self.clipboard = value

    def copy_clipboard(self, param):
        """Méthode pour copier le mdp ou le nom d'utilisateur

        PRE : reçoit un paramètre "mot de passe" ou "étudiant"(String)
        POST : copie le paramètre demande dans le clipboard
        """

        self.clipboard_clear()
        if param == "username":
            self.clipboard_append(self.clipboard.strip().split(", ")[0])
            messagebox.showinfo(
                "Succès", "Le nom d'utilisateur a bien été copié!")
        elif param == "password":
            self.clipboard_append(self.clipboard.strip().split(", ")[-1])
            messagebox.showinfo("Succès", "Le mot de passe a bien été copié!")
