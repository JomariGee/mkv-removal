#!/usr/bin/env python3
import os
import send2trash

#----------------------------------------------
# Removes .mkv files from current directory 
#----------------------------------------------


# Establish the file path where videos .mkv videos will be deleted  
file_path= "C:/Users/mrjam/Videos/" 
files = os.listdir(file_path) 

# Loops through the directory to search for .mkv files and then moves them to the recycling bin 
for file_name in files:
	if file_name.endswith(".mkv"):
		os.path.join(file_path, file_name)
		#For permanent deletion -> os.remove(file_name)
		send2trash.send2trash(file_name)


"""
 Resources-that-helped
	1. https://www.codegrepper.com/code-examples/python/python+check+for+file+type
	2. https://stackoverflow.com/questions/32834731/how-to-delete-a-file-by-extension-in-python
	3. http://www.learningaboutelectronics.com/Articles/How-to-safely-delete-files-folders-using-the-send2trash-module-in-Python.php
""" 
