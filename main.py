"""Execution de l'application du gestionnaire de mot de passe"""

import Classes.utilities.utilities
from Classes.notes import ex_notes

print(Classes.utilities.utilities.password_gen())
# Run main application
notepad = ex_notes.Notepad(width=800, height=600)
notepad.run()
