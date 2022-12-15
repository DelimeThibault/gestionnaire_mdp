"""Interface graphique Utilisateur"""
import tkinter as tk
import json
from tkinter import filedialog as fd
from pathlib import Path
from .application.application import Application


class Interface(tk.Tk):
    """Classes qui créée l'interface de l'application"""

    def __init__(self):
        tk.Tk.__init__(self)
        self.__this_width = 600
        self.__this_height = 400

        # Set icon
        try:
            self.iconbitmap(Path(r"Classes\interface\lock.ico"))
        except FileNotFoundError:
            print('Fichier introuvable.')
        except IOError:
            print('Erreur IO.')
        # Set title
        self.title("Gestionnaire de mots de passe")

        # Center the window
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # For left-align
        left = (screen_width / 2) - (self.__this_width / 2)

        # For right-align
        top = (screen_height / 2) - (self.__this_height / 2)

        # For top and bottom
        self.geometry(
            f'{self.__this_width}x{self.__this_height}+{int(left)}+{int(top)}')

        # Open default file location
        try:
            with open(Path(r"db/credentials.json"), encoding="utf-8") as file:
                data = json.load(file)
                print(data)
                self.creer_widgets()
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

    def creer_widgets(self):
        """Création du widget qui affiche le texte et le bouton pour quitter"""
        self.label = tk.Label(self, text="J'adore Python !")
        self.bouton = tk.Button(self, text="Quitter", command=self.quit)
        self.create = tk.Button(self, text="Ajouter test", command=Application.add_credentials(
            self, "Git", "Chris", "mdpnul"))
        self.label.pack()
        self.bouton.pack()
        self.create.pack()

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
