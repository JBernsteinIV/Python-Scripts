#!/usr/bin/python

"""
This shell script removes all the contents of a folder if the filename provided is a folder. Else it removes a file provided the name of the file.
"""

import os     #To invoke system commands from Python script.
import sys    #To access sys.argv to check argument count for CLI.
import shutil #To access rmtree method that will delete contents of directory.

def usage():
	print('Usage: {} <FILE NAME>'.format(sys.argv[0]))
	sys.exit(1)

def isdir(path):
	try:
		shutil.rmtree(path)
	except OSError as e:
		print("Error: %s - %s." % (e.filename, e.strerror))
def writable(filename):
	return os.path.exists(filename) and os.access(filename, os.W_OK)

def authorized(filename):
	if "-f" in sys.argv:
		return True
	user_input = raw_input("Warning: This will permanently delete the file. Do you wish to continue (Y/N)?")
	return user_input == 'Y' or user_input == 'y' 

def removeIt(filename):
	if len(sys.argv) < 2:
		usage()
	else:
		fd = sys.argv[1]
		if authorized(fd) == True:
			if writable(fd) and not os.path.isdir(fd):
				os.remove(fd)
			else:
				isdir(fd)
		sys.exit(0)

if len(sys.argv) < 2:
	usage()
else:
	removeIt(sys.argv[1])
