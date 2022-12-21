"""Execution de l'application du gestionnaire de mot de passe"""
from interface import login


app = login.PasswordManager()
app.mainloop()
