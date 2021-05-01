# Readme Generator

We are bored of write the same things once and once again. We trust in the comments made inside of our files, and we decided to automate the boring stuff. 

Why to use this? Quick, Easy, Automatic: Only once three questions.

![](https://miro.medium.com/max/500/1*TKt92huSBbSnbRNuAVTx_A.jpeg)

## Description

The readmeg writes the basic structure of a readme file filling all the content and getting ready to show the awesome code that you do. It includes title, description, files, environment, and authors. 

## Installation

Move the file readmeg.py to the path /usr/local/bin. If you are in linux, you can use the next command:
```
$ cp readmeg.py readmeg && sudo mv readmeg.py /usr/local/bin
```

## How to use

You need to go to the directory where you want to create the readme file. Then you can type this in the command line:
```
$ readmeg
```
or
```
$ readmeg The description of the reporitory
```

## What readme's section are included?
### Title
  Readmeg takes the name of the directory, replace special characters for spaces, and capitalize the name.
### Description
  It is a general description of the repository. readmeg ask the user what it is.
### Files
  It includes a spreadsheet with the names and descriptions of every file and function in the directory, specially man pages, C header files, C functions, and Python scripts (and counting). The description of this files are based on the description of the file written inside each file, looking like this:
|File|Description|
|:-:|:-:|
|file1|Description depending on the type of the file.|
#### Python scripts
  Takes the first multiline comment, surrounded by """ or by ''' as description.

#### C functions
  Takes all the multiline comments of the file to list all the functions written in the file. The comments needs to match the format required by the ANSI 90 standard:
```
/**
* function_name - first line of description
* second line of description (optional)
* @parameter (optional)
* Return: returned value (optional)
*/
```
Let us know which other kind of programming files you want us to automate here: https://twitter.com/NaVeDuran1 

### Environment

The first time the program is executed is going to ask you the environ where the repository was developed.
If you are from Holberton write:
'''
Ubuntu 14.06.6 LTS
'''

### Authors

Readmeg reads the git configuration variables 'user.fullname', 'user.email' and 'user.environ'. If those aren't created, readmeg asks the full name of the user.

### Changing Author, Email or Environment:

Type this commands to change the information that is going to be included in your subsequent readmes:

'''
$ git config --config user.fullname My New Name
'''

'''
$ git config --config user.email my_new@email.com
'''

'''
$ git config --config user.environ my-environment
'''

This will not change the readmes created previously.

## Files
The files contained in this repository are:

|File|Description|
|:-:|:-:|
|README.md| This are the instructions for use, non writtable for avoid mistakes.|

## Environment
This project has been tested on Ubuntu 14.06.6 LTS
## Version
Released on April 29th of 2021.

## Authors
* **Nicolás Urrea Rangel:** - [Email](nico15935746@gmail.com)
* **Natalia Vera Duran:** - [Email](naveduran@gmail.com)
