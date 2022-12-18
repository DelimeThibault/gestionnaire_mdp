import tkinter as tk
from tkinter import messagebox
from pathlib import Path
#from tkinter import simpledialog
from .application import application
import json


class PasswordManager(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        # Créer une fenêtre principale
        self.geometry('250x150')
        self.title("Gestionnaire de mots de passe")

        # Open default file location
        try:
            with open(Path(r"db/credentials.json"), encoding="utf-8") as file:
                data = json.load(file)
                print(data)
                self.password_database = data
        except FileNotFoundError:
            self.label = tk.Label(self, text='Pas de fichier trouvé')
            self.label.pack()
            # self.select_file()
            # open button
            self.open_button = tk.Button(
                self,
                text='Open a File',
                command=self.select_file
            )

            self.open_button.pack(expand=True)

        # Set icon
        try:
            self.iconbitmap(Path(r"interface\lock.ico"))
        except FileNotFoundError:
            print('Fichier introuvable.')
        except IOError:
            print('Erreur IO.')


        # Afficher la page de login
        self.show_signup_page()

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
        self.question_label = tk.Label(self.signup_frame, text="Question personnelle:")
        self.question_label.pack()
        self.question_entry = tk.Entry(self.signup_frame, width=30)
        self.question_entry.pack()

        # Créer un bouton pour s'inscrire
        self.signup_button = tk.Button(self.signup_frame, text="S'inscrire", command=self.signup)
        self.signup_button.pack()

        # Créer un bouton si on est déja inscrit
        self.already_signup_button = tk.Button(self.signup_frame, text="Déja inscit", command=self.show_login_page)
        self.already_signup_button.pack()

    def signup(self):
        # Récupérer le mot de passe et la question personnelle entrés par l'utilisateur
        password = self.password_entry.get()
        question = self.question_entry.get()

        # Vérifier si le mot de passe et la question personnelle sont valides (par exemple, s'assurer qu'ils ne sont pas vides)
        if password == "" or question == "":
            messagebox.showerror("Erreur", "Mot de passe et question personnelle sont obligatoires")
            return

        # Vérifier si l'utilisateur est déjà enregistré dans la base de données
        if question in self.password_database:
            messagebox.showerror("Erreur", "L'utilisateur est déjà enregistré")
            return

        # Enregistrer le mot de passe et la question personnelle dans la base de données
        self.password_database[question] = password
        print(self.password_database)

        # Afficher un message de confirmation et passer à la page de login
        messagebox.showinfo("Succès", "Inscription réussie!")
        self.show_login_page()

    def show_login_page(self):
        # Détruire la page de signup
        self.signup_frame.destroy()
        # Créer un cadre pour afficher le formulaire de login
        self.login_frame = tk.Frame(self)
        self.login_frame.pack()

        # Créer une étiquette et un champ de saisie pour le mot de passe
        self.password_label = tk.Label(self.login_frame, text="Mot de passe:")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.login_frame, show="*", width=30)
        self.password_entry.pack()

        # Créer un bouton pour se connecter
        self.login_button = tk.Button(self.login_frame, text="Se connecter", command=self.login)
        self.login_button.pack()

    def login(self):
        # Récupérer le mot de passe entré par l'utilisateur
        password = self.password_entry.get()

        # Vérifier si le mot de passe est correct
        if password == "ok":
            # Si le mot de passe est correct, afficher la page principale
            self.show_main_page()
        else:
            # Si le mot de passe est incorrect, afficher un message d'erreur
            messagebox.showerror("Erreur", "Mot de passe incorrect")
    #def show_info(self):

    def add_info(self):
        # Créer un cadre pour ajouter les infos
        self.add_frame = tk.Toplevel(self)
        self.add_frame.title("Nouvelle page")
        self.add_frame.pack()

        # Créer une étiquette et un champ de saisie pour le mot de passe
        self.site_label = tk.Label(self.add_frame, text="Site:")
        self.site_label.pack()
        self.site_entry = tk.Entry(self.add_frame, width=30)
        self.site_entry.pack()
        print(self.site_entry.get())
        self.username_label = tk.Label(self.add_frame, text="Nom d'utilisateur:")
        self.username_label.pack()
        self.username_entry = tk.Entry(self.add_frame, width=30)
        self.username_entry.pack()
        self.password_label = tk.Label(self.add_frame, text="Mot de passe: \n (si vous n'en entrer pas, un mot de passe fort sera automatiquement créé)")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.add_frame, show="*", width=30)
        self.password_entry.pack()
        self.password_list_frame = tk.Frame(self.geometry('1200x450'))
        self.password_list_frame.pack()

        # Créer un bouton pour ajouter
        self.add_button = tk.Button(self.add_frame, text="Ajouter", command=lambda: application.Application.add_credentials(self, self.site_entry.get(), self.username_entry.get(), self.password_entry.get()))
        #self.add_button.bind("<enter>", application.Application.add_credentials(self, self.site_entry.get(), self.username_entry.get(), self.password_entry.get()))
        self.add_button.pack()

    '''def edit_password(self):
        selection = self.password_list.curselection()
        if selection:
            index = selection[0]
            identification_list[index] = (username_entry.get(), password_entry.get())
            username_entry.delete(0, "end")
            password_entry.delete(0, "end")
            update_list()'''

    '''def delete_password():
        selection = self.password_list.curselection()
        if selection:
            index = selection[0]
            del identification_list[index]
            update_list()'''

    '''def copy_password():
        selection = self.password_list.curselection()
        if selection:
            index = selection[0]
            root.clipboard_clear()
            root.clipboard_append(identification_list[index][1])'''

    def show_main_page(self):
        # Détruire la page de login
        self.login_frame.destroy()

        # Créer un cadre pour afficher la liste des mots de passe enregistrés et les widgets associés
        self.password_list_frame = tk.Frame(self.geometry('1200x300'))
        self.password_list_frame.pack()
        self.password_list_label = tk.Label(self.password_list_frame, text="Mots de passe enregistrés:")
        self.password_list_label.pack()
        self.password_list = tk.Listbox(self.password_list_frame, height=10, width=50)
        self.password_list.pack()

        # Mettre à jour la liste des mots de passe enregistrés
        #self.update_password_list()

        # Créer un bouton pour copier le mot de passe sélectionné dans le presse-papiers
        self.copy_password_button = tk.Button(self.password_list_frame, text="Copier le mot de passe")#,command=self.copy_password
        self.copy_password_button.pack(side="left")

        # Créer un bouton pour ajouter un nouveau mot de passe
        self.add_password_button = tk.Button(self.password_list_frame, text="Ajouter un mot de passe",command=self.add_info)
        self.add_password_button.pack(side="left")

        # Créer un bouton pour modifier le mot de passe sélectionné
        self.edit_password_button = tk.Button(self.password_list_frame, text="Modifier le mot de passe")#, command=self.edit_password
        self.edit_password_button.pack(side="left")

        # Créer un bouton pour supprimer le mot de passe sélectionné
        self.delete_password_button = tk.Button(self.password_list_frame, text="Supprimer le mot de passe")#,command=self.delete_password
        self.delete_password_button.pack(side="left")

if __name__ == "__main__":
    password_manager = PasswordManager()
    password_manager.mainloop()
