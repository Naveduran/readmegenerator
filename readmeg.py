#!/usr/bin/python3
'''This program creates a readme file for github projects who include \
programs in C or Python, assuming it has only one author, whose name is going \
to be asked the first time this program is executed.'''
from os import popen
from sys import argv


print("COMMENT YOUR FILES PROPERLY BEFORE USING THIS FUNCTION")

headers = []
manuals = []
title = popen("pwd").read().split("/")[-1].replace("-", "").replace("_", "").\
        title()
files = popen("ls ").read().split("\n")[:-1]
if files == []:
    print("There aren't files in the working directory")

author = popen("git config --get user.fullname").read()[:-1].title()
email = popen("git config --get user.email").read()[:-1]
environ = popen("git config --get user.environ").read()[:-1]
if author == '':
    popen("git config --global user.fullname \"{}\"" .format(input("Write \
    your full name:")))
if email == '':
    popen("git config --global user.email \"{}\"" .format(input("Write \
    your github email:")))
if environ == '':
    popen("git config --global user.environ \"{}\"" .format(input("Write \
    environ:")))

if len(argv) < 2:
    descript = input("Write a description of the repository in one line:\n")
else:
    descript = " ".join(argv[1:])

while descript[0] == " ":
    descript = descript[1:]
descript = descript.capitalize()
while descript[-1] == " ":
    descript = descript[:-1]
if descript[-1] != ".":
    descript += "."

text = "# {}\n## Description\n{}\n\n## Files\nThe files contained in this \
repository are:\n\n|File|Description|\n|:-:|:-:|\n".\
format(title, descript)

for file in files:
    if file[:3] == 'man':
        text += "|{}|Contains the manual to use the program with detailed \
        description, required parameters, functioning, and return \
        values.\n". format(manuals)
    elif file[-2:] == '.h':
        text += "|{}|Contains all the functions and macros that are going\
        to be included in the program, individually created for this program,\
        or inherited from the standard libraries|\n". format(file)
    elif file[-3:] == '.py' or file[-2:] == '.c':
        if file[-3:] == '.py':
            if file == 'readmegenerator.py':
                pass
            description = popen("cat {}".format(file)).read()
            splitted = description.split("'''")
            if len(splitted) == 1:
                splitted = description.split('"""')
            description = splitted[1].replace("\\","").replace("\n"," ").\
                          replace("  "," ")
        elif file[-2:] == '.c':
            description = str(popen("awk \
             '/\*\* */,/\* @/||/eturn/||/ \*\//||/ \* \*/' {}".format(file)).\
             read().split("\n")[1:-2])[2:-2].split("-")[1].\
                replace("', '", " ").replace(" *", "")
        while description[0] == " ":
            description = description[1:]
        description = description.capitalize()
        while description[-1] == " ":
            description = description[:-1]
        if description[-1] != ".":
            description += "."
        text += "|{}|{}|\n".format(file, description)
    else:
        text += "|{}||\n".format(file)

text += "\n## Environment\nThis project has been tested on {} \
LTS\n\n## Authors\n* **{}:** - [Email]({})\n" .format(environ, author, email)

with open("README.md", "w+") as file:
    file.write(text)

with open("README.md", "r") as file:
    if file.read():
        print("The readme was created successfully!!!")
    else:
        print("Error: The readme wasn't created")
