#!/usr/bin/env python3
import os

#----------------------------------------------
# Removes .mkv files from current directory 
#----------------------------------------------


# Establish the file path where videos .mkv videos will be deleted  
file_path= "C:/Users/mrjam/Videos/" 
files = os.listdir(file_path) 

# Loops through the directory to search for .mkv files and then deletes them
for file_name in files:
	if file_name.endswith(".mkv"):
		os.remove(os.path.join(file_path, file_name))


"""
 Resources-that-helped
	1. https://www.codegrepper.com/code-examples/python/python+check+for+file+type
	2. https://stackoverflow.com/questions/32834731/how-to-delete-a-file-by-extension-in-python
""" 