"""Execution de l'application du gestionnaire de mot de passe"""
from packages.interface import gui
from packages.utilities.password_function import password_generation
# from packages.utilities import utilities
# from packages.notes import notes
print(password_generation())
# Run main application
# notepad = notes.Notepad(width=800, height=600)
# notepad.run()


if __name__ == "__main__":
    app = gui.Application()
    # app.title("Gestionnaire de mots de passe")
    app.mainloop()
