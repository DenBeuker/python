#! /usr/bin/env python3
# Automate The Boring Stuff Practice Projects - Chapter 10
# fileRemover.py - Walks through a folder tree and searches for exceptionally large files 
# or folders and prints them to the screen

import os
user_dir = input("Specify a directory you want to search(abs path): ") 
file_size = int(input("Specify a filesize you want to check for(bytes): "))

for dirName, subDir, fileNames in os.walk(user_dir):
    for fname in fileNames:
        full_path = dirName + "\\" + fname
        
        if os.path.getsize(full_path) > file_size:
            print(full_path, end=' ')
            print("\t\t", os.path.getsize(full_path), " Bytes")
