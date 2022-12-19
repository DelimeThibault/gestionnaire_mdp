import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog as fd
from pathlib import Path
# from tkinter import simpledialog
from .application import application
import json
from json.decoder import JSONDecodeError


class PasswordManager(tk.Tk):
    """Interface graphique avec Tkinter"""

    def __init__(self):
        tk.Tk.__init__(self)
        # Créer une fenêtre principale
        self.__this_width = 250
        self.__this_height = 150
        self.title("Gestionnaire de mots de passe")
        self.password_database = dict()
        self.signin_database = dict()
        self.center_window(self.__this_width, self.__this_height)
        self.clipboard = ""
        # Ouvre le fichier contenant les mdp
        try:
            with open(Path(r"db/credentials.json"), encoding="utf-8") as file:
                data = json.load(file)
                self.password_database = data
        except FileNotFoundError:
            self.label = tk.Label(self, text='Pas de fichier trouvé')
            self.label.pack()
            self.open_button = tk.Button(
                self,
                text='Open a File',
                command=self.select_file
            )

            self.open_button.pack(expand=True)
        except JSONDecodeError:
            pass

        # Ouvre le fichier contenant les mdp singin
        try:
            with open(Path(r"db/signin.json"), encoding="utf-8") as file:
                data = json.load(file)
                self.signin_database = data
                self.show_login_page()
        except FileNotFoundError:
            self.label = tk.Label(self, text='Pas de fichier trouvé')
            self.label.pack()
            self.open_button = tk.Button(
                self,
                text='Open a File',
                command=self.select_file
            )

            self.open_button.pack(expand=True)
        except JSONDecodeError:
            self.show_signup_page()

        # Change l'icône
        try:
            self.iconbitmap(Path(r"interface\lock.ico"))
        except FileNotFoundError:
            print('Fichier introuvable.')
        except IOError:
            print('Erreur IO.')

        # Afficher la page de login
        # self.show_signup_page()

    def center_window(self, width, height):
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
        # Récupérer le mot de passe et la question personnelle entrés par l'utilisateur
        password = self.password_entry.get()
        question = self.question_entry.get()

        # Vérifier si le mot de passe et la question personnelle sont valides (par exemple, s'assurer qu'ils ne sont pas vides)
        if password == "" or question == "":
            messagebox.showerror(
                "Erreur", "Mot de passe et question personnelle sont obligatoires")
            return

        # Vérifier si l'utilisateur est déjà enregistré dans la base de données
        # if question in self.signup_database:
        #    messagebox.showerror("Erreur", "L'utilisateur est déjà enregistré")
        #    return

        # Enregistrer le mot de passe et la question personnelle dans la base de données
        self.signin_database["password"] = password
        self.signin_database["question"] = question

        try:
            with open(Path(r"db/signin.json"), 'w', encoding="utf-8") as file:
                json.dump(self.signin_database, file,
                          sort_keys=True, indent=4)
        except FileNotFoundError:
            return ("ERROR DB NOT FOUND")

        # Afficher un message de confirmation et passer à la page de login
        messagebox.showinfo("Succès", "Inscription réussie!")
        self.show_login_page()
        self.signup_frame.destroy()

    def show_login_page(self):

        # Créer un cadre pour afficher le formulaire de login
        self.login_frame = tk.Frame(self)
        self.center_window(340, 90)
        self.login_frame.pack()

        # Créer une étiquette et un champ de saisie pour le mot de passe
        self.password_label = tk.Label(
            self.login_frame, text="Mot de passe:\n (Si vous vous ne souvenez pas de votre mot de passe, tapez o.)")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.login_frame, show="*", width=30)
        self.password_entry.pack()

        # Créer un bouton pour se connecter
        self.login_button = tk.Button(
            self.login_frame, text="Se connecter", command=self.login)
        self.login_button.pack()

    def show_question_page(self):
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
            self.add_frame, text="Mot de passe: \n (si vous n'en entrer pas, un mot de passe fort sera automatiquement créé)")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.add_frame, show="*", width=30)
        self.password_entry.pack()
        self.password_list_frame = tk.Frame()
        # self.geometry('1200x450')
        #self.center_window(1200, 450)
        self.password_list_frame.pack()

        # Créer un bouton pour ajouter
        self.add_button = tk.Button(self.add_frame, text="Ajouter", state="disabled", command=lambda: self.add_password(
            self.site_entry.get().upper(), self.username_entry.get(), self.password_entry.get()))
        self.add_button.pack()

        def update(*args):
            if len(my_site.get()) == 0 or len(my_user.get()) == 0:
                self.add_button.config(state="disabled")
            else:
                self.add_button.config(state="normal")
        my_user.trace('w', update)
        my_site.trace('w', update)

    def edit_password(self):
        self.modif_frame = tk.Toplevel(self)
        self.modif_frame.title("Modifier un mot de passe")
        self.selected_site = ""
        self.listbox_site = tk.Listbox(self.modif_frame)
        self.listbox_site.pack()
        self.listbox_site.bind('<<ListboxSelect>>', self.change_site)
        for site in self.password_database:
            self.listbox_site.insert(tk.END, site)

        # ,command=lambda:select_credentials())
        self.site_btn = tk.Button(
            self.modif_frame, state="disabled", text="Suivant", command=self.select_username)
        self.site_btn.pack()

    def change_site(self, evt):
        """Stocke la valeur sélectionnée dans un attribut self.selected_site"""
        w = evt.widget
        index = int(w.curselection()[0])
        value = w.get(index)
        if value != "":
            self.selected_site = value
            self.site_btn.config(state="normal")

    def change_user(self, evt):
        """Stocke la valeur sélectionnée dans un attribut self.selected_user"""
        w = evt.widget
        index = int(w.curselection()[0])
        value = w.get(index)
        if value != "":
            self.selected_user = value
            self.cred_btn.config(state="normal")

    def select_username(self):
        self.modif_frame.destroy()
        self.username_frame = tk.Toplevel(self)
        self.username_frame.title('Modifier un mot de passe')
        self.selected_user = ""
        self.listbox_cred = tk.Listbox(self.username_frame)
        self.listbox_cred.pack()
        self.listbox_cred.bind('<<ListboxSelect>>', self.change_user)
        for username in self.password_database[self.selected_site]:
            self.listbox_cred.insert(
                tk.END, username)

        self.cred_btn = tk.Button(
            self.username_frame, state="disabled", text="Modifier", command=self.modify_credentials)
        self.cred_btn.pack()

    def modify_credentials(self):
        self.username_frame.destroy()
        self.modify = tk.Toplevel(self)
        self.modify.title('Modifier informations')
        my_user = tk.StringVar(self.modify)
        my_pwd = tk.StringVar(self.modify)
        self.label_site = tk.Label(
            self.modify, text="Nouveau nom d'utilisateur (n'écrivez rien si vous voulez le conserver)")
        self.label_site.pack()
        self.user_entry = tk.Entry(self.modify, textvariable=my_user)
        self.user_entry.pack()
        self.label_pwd = tk.Label(self.modify, text="Nouveau mot de passe")
        self.label_pwd.pack()
        self.pwd_entry = tk.Entry(self.modify, textvariable=my_pwd)
        self.pwd_entry.pack()
        self.new_user = self.selected_user
        self.new_pwd = ''

        # Bouton pour modifier
        self.button = tk.Button(
            self.modify, text="Mettre à jour", command=self.update_credentials)
        self.button.pack()

        def update(*args):
            if len(my_user.get()) == 0:
                self.new_user = self.selected_user
                if len(my_pwd.get()) == 0:
                    self.new_pwd = application.Credentials.password_generation()
                else:
                    self.new_pwd = my_pwd.get()
            elif len(my_user.get()) > 0:
                self.new_user = my_user.get()
                if len(my_pwd.get()) == 0:
                    self.new_pwd = application.Credentials.password_generation()
                else:
                    self.new_pwd = my_pwd.get()
                del self.password_database[self.selected_site][self.selected_user]
        my_user.trace('w', update)
        my_pwd.trace('w', update)

    def update_list(self):
        self.sort_password()
        self.password_list.delete(0, "end")
        for site, credentials in self.password_database.items():
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
        # self.geometry('1200x300')
        self.center_window(590, 305)
        self.password_list_frame.pack()
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
            self.password_list_frame, text="Copier le mot de passe", command=self.copy_password)
        self.copy_password_button.pack(side="left")
        #self.copy_password_button.grid(column=0, row=0)

        # Créer un bouton pour ajouter un nouveau mot de passe
        self.add_password_button = tk.Button(
            self.password_list_frame, text="Ajouter un mot de passe", command=self.add_info)
        self.add_password_button.pack(side="left")
        #self.add_password_button.grid(column=1, row=0)

        # Créer un bouton pour modifier le mot de passe sélectionné
        self.edit_password_button = tk.Button(
            self.password_list_frame, text="Modifier le mot de passe", command=self.edit_password)
        self.edit_password_button.pack(side="left")
        #self.edit_password_button.grid(column=0, row=1)

        # Créer un bouton pour supprimer le mot de passe sélectionné
        self.delete_password_button = tk.Button(
            self.password_list_frame, text="Supprimer le mot de passe")  # ,command=self.delete_password
        self.delete_password_button.pack(side="left")
        #self.delete_password_button.grid(column=1, row=1)

    def select_file(self):
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
        new_pwd = application.Application.add_credentials(
            site, username, password)
        key = next(iter(new_pwd))
        user = next(iter(new_pwd[key]))
        infos = new_pwd[key]

        if key in self.password_database.keys():
            if user in self.password_database[key]:
                return ("Cet utilisateur existe déjà")
            else:
                self.password_database[key].update(infos)
        else:
            self.password_database[key] = infos
        # Ouvre le fichier contenant les mdp
        try:
            with open(Path(r"db/credentials.json"), 'w', encoding="utf-8") as file:
                json.dump(self.password_database, file,
                          sort_keys=True, indent=4)
        except FileNotFoundError:
            return ("ERROR DB NOT FOUND")

        self.update_list()
        self.add_frame.destroy()

    def search_password(self, site):
        """Cette fonction recherche un site dans la base de donnée"""
        if self.password_database[site]:
            for keys in self.password_database[site]:
                result = f"{site} : \n{keys} : {self.password_database[site][keys]}"
                return result
        else:
            return None

    def sort_password(self):
        dict_sort = dict(sorted(self.password_database.items())).copy()
        for i in dict_sort:
            print(i)
            dict_sort[i] = dict(sorted(dict_sort[i].items()))

        self.password_database = dict_sort

    def update_credentials(self):
        site = self.selected_site
        user = self.new_user
        if self.new_pwd == "":
            self.new_pwd = application.Credentials.password_generation()
        self.password_database[site][user] = self.new_pwd
        self.update_list()
        try:
            with open(Path(r"db/credentials.json"), 'w', encoding="utf-8") as file:
                json.dump(self.password_database, file,
                          sort_keys=True, indent=4)
        except FileNotFoundError:
            return ("ERROR DB NOT FOUND")
        self.modify.destroy()

    def selected_value(self, evt):
        w = evt.widget
        index = int(w.curselection()[0])
        value = w.get(index)
        if value != "":
            print(value)
            self.clipboard = value

    def copy_password(self):
        self.clipboard_clear()
        self.clipboard_append(self.clipboard.strip().split(", ")[-1])
