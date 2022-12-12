import tkinter as tk
import json
from tkinter import filedialog as fd


class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.__thisWidth = 600
        self.__thisHeight = 400

        # Set icon
        try:
            self.iconbitmap("Classes\interface\lock.ico")
        except:
            pass

        # Set title
        self.title("Gestionnaire de mots de passe")

        # Center the window
        screenWidth = self.winfo_screenwidth()
        screenHeight = self.winfo_screenheight()

        # For left-align
        left = (screenWidth / 2) - (self.__thisWidth / 2)

        # For right-align
        top = (screenHeight / 2) - (self.__thisHeight / 2)

        # For top and bottom
        self.geometry('%dx%d+%d+%d' % (self.__thisWidth,
                                       self.__thisHeight,
                                       left, top))

        # Open default file location
        try:
            file = open("db\credentials.json")
            data = json.load(file)
            file.close()
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

        self.label = tk.Label(self, text="J'adore Python !")
        self.bouton = tk.Button(self, text="Quitter", command=self.quit)
        self.label.pack()
        self.bouton.pack()

    def select_file(self):
        filetypes = (
            ('json files', '*.json'),
            ('All files', '*.*')
        )

        filename = fd.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes)
