#!/usr/bin/python3
'''This program creates a readme file for github projects who include \
programs in C or Python, assuming it has only one author, whose name is going \
to be asked the first time this program is executed.'''
from os import popen
from sys import argv

print("COMMENT YOUR FILES PROPERLY BEFORE USING THIS FUNCTION")

# Get the title from the name of the directory

title = popen("pwd")\
        .read()\
        .split("/")[-1]\
        .replace("-", " ")\
        .replace("_", " ")\
        .title()

# Get the names of the files from the directory

files = popen("ls ")\
        .read()\
        .split("\n")[:-1]

if files == []: #Prints a warning if the directory is empty
    print("There aren't files in the working directory")

# Bring the global variables author, email and environ

author = popen("git config --get user.fullname")\
         .read()[:-1]\
         .title()

email = popen("git config --get user.email")\
        .read()[:-1]

environ = popen("git config --get user.environ")\
          .read()[:-1]

# If there aren't the globals, create them asking the content to the user
# Only the first time for agility

if author == '':
    popen("git config --global user.fullname \"{}\""
          .format(input("Write your full name:")))

if email == '':
    popen("git config --global user.email \"{}\""
          .format(input("Write your github email:")))

if environ == '':
    popen("git config --global user.environ \"{}\""
          .format(input("Write environ:")))

# Ask for the general description of the repository and give the proper format

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

# Write the sections 'Title', 'Description' and the beginning of 'Files'

text = '''# {}\n## Description\n{}\n\n## Files\nThe files contained in 
this repository are:\n\n|File|Description|\n|:-:|:-:|\n'''
.format(title, descript)

# Write the names and description of the files in the table

for file in files:

# Description of man pages

    if file[:3] == 'man':
        text += '''|[{}](./{})|Contains the manual to use the program with
        detailed description, required parameters, functioning, and return 
        values.\n'''.format(file, file)

# Description of header files

    elif file[-2:] == '.h':
        text += '''|[{}](./{})|Contains all the functions and macros that
        are going to be included in the program, individually created for 
        this program, or inherited from the standard 
        libraries|\n'''.format(file, file)

# Don't include readme files in the list'

    elif file[] == 'README.md':
        pass

    elif file[-3:] == '.py' or file[-2:] == '.c':

# Description of python scripts

        if file[-3:] == '.py':

# Ignore this script when making the list of files

            if file == 'readmegenerator.py':
                pass
            description = popen("cat {}".format(file)).read()
            splitted = description.split("'''")
            if len(splitted) == 1:
                splitted = description.split('"""')
            description = splitted[1]\
                .replace("\\","")\
                .replace("\n"," ")\
                .replace("  "," ")

# Description of C functions
        elif file[-2:] == '.c':
            try: # THIS DON'T NEED TO BE READ
                c = '''awk '/\*\* */,/\* @/||/\*@/||
                /eturn/||/ \*\//||/ \* \*/' {}'''
                description = str(popen(c.format(file))
                                  .read()
                                  .split("\n")[1:-2])[2:-2]\
                    .split("-")[1]\
                    .replace("', '", " ")\
                    .replace(" *", "")
            except IndexError:
                print(file)
                pass

# Format description of the python files and C functions

        while description[0] == " ":
            description = description[1:]
        description = description.capitalize()
        while description[-1] == " ":
            description = description[:-1]
        if description[-1] != ".":
            description += "."
        text += "|[{}](./{})|{}|\n".format(file, file, description)
    else:
        text += "|[{}](./{})||\n".format(file, file)

# Write the Environment, and authors sections

text += "\n## Environment\nThis project has been tested on {} \
LTS\n\n## Authors\n* **{}:** - [Email]({})\n".format(environ, author, email)

# Create the readme file and write the content

with open("README.md", "w+") as file:
    file.write(text)

# Test if the readme written and returns a sucess message

with open("README.md", "r") as file:
    if file.read():
        print("The readme was created successfully!!!")
    else:
        print("Error: The readme wasn't created")
