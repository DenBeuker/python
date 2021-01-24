#! /usr/bin/env python3
# Automate The Boring Stuff Practice Projects - Chapter 9
# madlibs.py - Reads in a text file and changes all 
# ADJECTIVE, NOUN, ADVERB, or VERB(these actual words) into user supplied words

text = open('example.txt', 'r')
dotSplit = text.read()
result = ''.join([c for c in dotSplit if c not in ('.', '?', '!', ',')]) # Removes all punctuation 

spl = result.split() 
endlist = []
s = " "

for i in spl:
    if i == "ADJECTIVE":    
        q = input("Name an adjective: ")
        endlist += [q]
    elif i == "NOUN":
        q = input("Name a noun: ")
        endlist += [q]
    elif i == "VERB":
        q = input("Name a verb: ")
        endlist += [q]
    elif i == "ADVERB":
        q = input("Name an adverb: ")
        endlist += [q]
    else: 
        endlist += [i]

endlist = s.join(endlist) # endlist is still a list with all the words, we need to join them together to create 1 string/object
print(endlist)
fileName = input("How do you want to name the output file?: ") + ".txt"
new_file = open(fileName, "w")
new_file.write(endlist)
new_file.close()
text.close()

