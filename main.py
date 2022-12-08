"""Execution de l'application du gestionnaire de mot de passe"""

import Classes.utilities.utilities
from Classes.notes import notes

print(Classes.utilities.utilities.password_gen())
# Run main application
notepad = notes.Notepad(width=800, height=600)
notepad.run()
