"""Execution de l'application du gestionnaire de mot de passe"""
from interface import login


if __name__ == "__main__":
    app = login.PasswordManager()
    app.mainloop()
