#! /usr/bin/env python3
# Automate The Boring Stuff Practice Projects - Chapter 10
# selCopy.py - Walks through a folder tree and searches for files with a certain extension and copies them in a supplied folder
# Example: run selCopy.py
#          Will receive a prompt to specify path to search in, extension and where to copy them to
#          Example path: D:\, C:\Users\, C:\,...
#          Example extensions: txt, png, jpg,...
#          Example output folder: D:\Projects\copiedFiles (We create the copiedFiles dir here)

import os, shutil

def selectiveCopy(inputFolder, ext, outputFolder):
    for folderName, subFolder, filename in os.walk(inputFolder):
        for file in filename:
            if file.endswith(ext):
                filepath = os.path.join(os.path.abspath(folderName), file)
                if not os.path.exists(outputFolder):
                    #create result folder if it doesn't exist
                    os.makedirs(outputFolder)

                
                if os.path.dirname(filepath) != outputFolder:
                    #prevent copying files from result folder              
                    shutil.copy(filepath, outputFolder)
                    print(f'Copied {filepath} to result folder')



userInputFolder = input("Give a path(abs) to search files in: ")
userExtension = input("For what extension would you like to search?(txt,png,...): ")
userOutputFolder = input("Absolute path of output folder: ")
        
if __name__ == '__main__':
    selectiveCopy(userInputFolder, userExtension, userOutputFolder)