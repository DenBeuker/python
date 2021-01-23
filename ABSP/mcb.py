#! /usr/bin/env python3
# Automate The Boring Stuff Practice Projects - Chapter 9
# mcb.py - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.py save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.py <keyword> - Loads keyword to clipboard.
#        py.exe mcb.py list - Loads all keywords to clipboard.
#        py.exe mcb.py delete <keyword> - Deletes keyword.
#        py.exe mcb.py delete - Deletes all keywords.

import pyperclip, sys, shelve

mcbShelf = shelve.open('mcb')

# Checks if 2 arguments are given and checks the 1st arg to be save
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()   # Saves clipboard with name of the second argument
# Checks if 2 arguments are given and checks the 1st arg to be delete  
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    del mcbShelf[sys.argv[2]]       # Deletes key specified after delete
# Checks if there is only one argument given
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'delete':     # If the argument is delete then we delete ALL entries
        confirmation = input('Are you sure you want to delete all the keys? (Y/N)')
        if confirmation.lower() == 'y':
            mcbShelf.clear()
    elif sys.argv[1].lower() == 'list':       # If the argument is list we copy the keys to the clipboard
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:             # Only 1 argument => copies contents of that key to clipboard
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()

