#!/usr/bin/python

"""
This module is an introduction to Python's testing libraries.

Most of this code originates from Albert Sweigart's PyBay2017 tech conference 'Logging and Testing and Debugging, Oh My!'.
Source: https://www.youtube.com/watch?v=ONCVvS-gDMA

logging - Set up logs and log levels for debugging scripts.
pdb - Python Debugger
doctest - Helps in creating documentation. 

LOGGING
-------
import logging
LOGGING LEVELS:
	1. DEBUG - Only when something has gone wrong (e.g. incorrect output)
	2. INFO - Record of normal events (stuff you typically expect)
	3. WARN - Things to be cautious about (e.g. rounding errors)
	4. ERROR - Serious errors (e.g. segfault thrown)
	5. CRITICAL - Very bad errors (e.g. server is down and cannot be restarted)

PDB
---
import pdb
pdb = Python Debugger
	set_trace() - Runs a stack trace of your code.
		in set_trace()'s shell, we can use the following expressions:
			s = Step into
			n = Next / step over
			r = Return / step out
			c = Continue (until breakpoint is hit)
			l = Line (where is instruction pointer currently?)
			b = Breakpoint (Specify line number or function name to establish where to set breakpoint)
			cl = Clear breakpoint (specify breakpoint number)
			q = Quit pdb shell

DOCTEST
-------
import doctest
The doctest utility allows multi-line comments in Python ('''MESSAGE HERE''') to be extracted and turned into separate documentation files. This is useful for constructing manpages on scripts / system commands you might create.
NOTE: Doctest is NOT a replacement for the unittest module or unit testing with another library. Doctest should really just be used for initial testing. Other testing libraries provide far more customization with setting up and tearing down tests / assertions.

Tip from Albert Sweigart on doctest: Use doctest to test that your *documentation* is up to date. Use another testing library like unittest to make sure your code actually performs as intended.

	1. testmod() - Test module.
	2. 
"""
import doctest
import logging
import os
import pdb
import sys
import time

# The following is built to purposefully fail to showcase doctest's use case.
# Change the 5 underneath addTwoNumbers(2,2) in order to pass doctest's testing.
def addTwoNumbers(a,b):
	'''
	Returns the sum of a and b.

	>>> addTwoNumbers(2,2)
	5
	>>> addTwoNumbers(4,2)
	6
	'''
	return a + b

def trace(arguments):
	if "--trace" in arguments:
		logging.basicConfig(filename='logfile.txt', level=logging.DEBUG)
		pdb.set_trace()

def test(arguments):
	if "--test" in arguments:
		doctest.testmod()

if __name__ == '__main__':
	arguments = sys.argv
	trace(arguments)
	test(arguments)
	name = raw_input("Enter your name: ")
	print("Hello, %s\n" % (name))
	leftNumber = int(input("Enter first number: "))
	rightNumber = int(input("Enter second number: "))

	print("%s + %s = %s" % (leftNumber, rightNumber, (leftNumber + rightNumber)))
