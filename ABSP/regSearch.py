#! /usr/bin/env python3
# Automate The Boring Stuff Practice Projects - Chapter 9
# regSearch.py - opens all .txt files in a folder and searches for any line that matches a user-supplied regular expression

import re, os, glob  

folder_path = 'D:\AutomateTheBoringStuffWithPython\PracticeProjects\Chapter 9'
user_path = input("Give absolute path for folder: ")
user_search = input("What would you live to search for? ")

for filename in glob.glob(os.path.join(user_path, '*.txt')):
  with open(filename, 'r', encoding='utf-8') as f:
    text = f.read()
    huh = re.findall(user_search, text)   
    if len(huh) > 0:
        print(filename)
        print(huh)
        
        
        


