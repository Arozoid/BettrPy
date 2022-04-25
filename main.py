# BettrPy - v1.0 #

# This is a project made by Arozoid, made to make python easier to use.
# It is a simple, and small module that makes things look more clean.

import random
import math
import os
import sys
from subprocess import *
import wget
import threading
import platform
import readline
import webbrowser

# cubed() #
# Simple function that cubes the inputted number
def cubed(num):
	try:
		return num**3
	except:
		print("betterpython: An error occured while cubing the number")
		print("betterpython: Maybe you inputted a string?")

# squared() #
# Simple function that squares the inputted number
def squared(num):
	try:
		return num**2
	except:
		print("betterpython: An error occured while squaring the number")
		print("betterpython: Maybe you inputted a string?")

# printlst() #
# Instead of printing a list normally, which appears as ['1', '2']
# it appears as 1, 2
def printlst(list):
	try:
		print(', '.join(map(str, list)))
	except:
		print("betterpython: An error occured while printing the result")
		print("betterpython: Maybe you inputted something that was not a list?")

def printfile(path):
	try:
		file = fileman.read(path)
		print(f"O {path}\n|", '| '.join(map(str, file)))
	except:
		print("betterpython: An error occured while printing the result")
		print("betterpython: Maybe the file doesnt exist?")


# sqrt() #
# Simple function that finds the square root of the specified number
def sqrt(num):
	try:
		return math.sqrt(num)
	except:
		print("betterpython: An error occured while getting the answer")
		print("betterpython: Maybe you inputted a string?")

# randint() #
# Simple function that gets a random number between the two numbers inputted.
def randint(num, num2):
	try:
		return random.randint(num, num2)
	except:
		print("betterpython: An error occured while choosing the number")
		print("betterpython: Maybe you inputted a string?")

# isfile() #
# Finds the specified file.
def isfile(file):
	return os.path.isfile(file)

# isdir() #
# Finds the specified directory.
def isdir(direct):
	return os.path.isdir(direct)

# fdexist() #
# Finds the specified file or directory.
def fdexist(file):
	return os.path.exists(direct)

'''fileman: Simple file manager'''
class fileman():
	# read() #
	# Reads the contents of a file.
	def read(self, path):
		try:
			with open(path, "r") as f:
				return f.readlines()
		except:
			print("betterpython: fileman: An error occured while reading this file.")
			print("betterpython: fileman: Maybe you entered the wrong path?")

	# mkfile() #
	# Creates an empty file
	def mkfile(self, name, direct):
		try:
			with open(f'{direct}{name}', 'w+') as file:
				file.write('')
			print("Made file sucessfully!")
		except:
			print("betterpython: fileman: An error occured while making the file.")
			print("betterpython: fileman: Maybe you messed up the directory path?")

	# mkdir() #
	# Creates a directory in the directory specified.
	def mkdir(self, name, direct):
		try:
			os.chdir(direct)
			os.mkdir(name)
			print(f"Directory '{name}' was created.")
		except:
			print("betterpython: fileman: An error occured while making the directory.")
			print("betterpython: fileman: Maybe the directory you were trying to make it in was invalid?")

	# rmfile() #
	# Removes a file.
	def rmfile(self, path):
		try:
			os.remove(path)
			print("Sucessfully removed.")
		except:
			print("betterpython: fileman: The file you were going to remove doesnt exist.")

	# ls() #
	# Looks in the specified directory.
	def ls(self, direct):
		try:
			os.chdir(direct)
			return os.listdir()
		except:
			print("betterpython: fileman: An error occured while looking at the directory")
			print("betterpython: fileman: Maybe the directory you inputted was invalid?")
  
  	def mvfile(name,orgin,directory):
    	try:
      	os.rename(f"{origin}{name}", f"{directory}{name}")
    	except:
      	print("betterpython: fileman: An error occured while moving the file")
				print("betterpython: fileman: Maybe the directory(s) or name you inputted was invalid?")
  
	# rmdir() #
	# Removes an empty directory.
	def rmdir(self, direct):
		try:
			os.rmdir(direct)
			print(f"Removed directory '{direct}'.")
		except:
			print("bettrpy: fileman: An error occured while removing the directory")
			print("bettrpy: fileman: Maybe the directory was not empty?")

	# append() #
	# Appends the specified string to the specified file.
	def append(self, write, path):
		try:
			with open(path, "a") as f:
				f.write(write)
			print("Sucessfully appended to file.")
		except:
			print("betterpython: fileman: An error occured while appending to file.")
			print("betterpython: fileman: Maybe the file you were trying to access doesnt exist?")

	# write() #
	# Erases the whole file and writes the specified string to it.
	def write(self, write, path):
		try:
			with open(path, "w") as f:
				f.write(write)
			print("Sucessfully wrote to file.")
		except:
			print("betterpython: fileman: An error occured while writing to file.")
			print("betterpython: fileman: Maybe the file you were trying to access doesnt exist?")

	# make_exec #
	# Makes specified file executable.
	def make_exec(self, path):
		Popen(f"chmod +x {path}", shell=True)

	# wget() #
	# Gets a file from the web.
	def wget(self, directory="", url=""):
		try:
			urlfix = url
			if "https://" or "http://" not in url:
				urlfix = f"https://{url}"
			wget.download(urlfix, out = directory)
			print(f"Successfully downloaded from {url}.")
		except:
			print("Python wget is either not installed or not working. To install python wget, use 'pip install wget'")

	# fhas #
	# Checks if a file has a specified string.
	def fhas(self, string, path):
		with open(path, "r") as f:
			for line in f:
				if string in line:
					return True
		return False

	# dirhas() #
	# Checks if the specified directory has a file.
	def dirhas(self, file, directory):
		listd = fileman.ls(directory)
		for things in listd:
			if file in listd:
				return True
		return False

fileman = fileman()

# terminal() #
# Runs the specified command in a virtual terminal
def terminal(command, workingdir):
	Popen(command, shell=True, cwd=workingdir)

'''Cachier - Caches values in a file.'''
class cachier:
  def create(cache="default"):
    with open(f"{cache}.cache","w+") as f:
      f.write("")

  def flush(cache="default"):
    with open(f"{cache}.cache","w+") as f:
      f.write("")

  def add(value, cache="default"):
    if not os.path.isfile(f"{cache}.cache"):
      cachier.create("time")
    with open(f"{cache}.cache","a") as f:
      f.write(f"{value},")

  def read(cache="default"):
    if not os.path.isfile(f"{cache}.cache"):
      cachier.create("time")
    with open(f"{cache}.cache","r") as f:
      for line in f:
        memory_l = []
        memory_l = line.split(",")
        memory_l.pop()
        return memory_l

'''bettervar - Allows creation and deletion and reading of betterpython variables.'''
'''BettrPy variables are basicly infinite. Normal variables cannot also be deleted.'''
variable_list = {}

class bettervar:
    def exist(variable):
        if variable in variable_list:
            return True
        else:
            return False

    def get(variable):
        return variable_list.get(variable)

    def create(variable, value):
      if not bettervar.exist(variable):
        variable_list[variable] = value

    def remove(variable):
        variable_list.pop(variable)

    def update(variable, value):
        if bettervar.exist(variable):
            variable_list.update({variable: value})

'''knitter - Allows infinite creation of threads'''
thread_list = {}

class knitter():
  def make(thread,func,args):
    thread_list[thread] = threading.Thread(target=func,args=args)

  def start(thread,join=True):
    thread_list[thread].start()
    if join:
      thread_list[thread].join()

  def delete(thread):
    thread_list.pop(thread)

'''tpainter - Allows simple terminal colors'''
class tpainter:
	def fg(color_num=15):
		if color_num == "reset":
			return '\u001b[38;5;255m'
		return f'\u001b[38;5;{color_num}m'

	def bg(color_num=0):
		if color_num == "reset":
			return '\u001b[48;5;0m'
		return f'\u001b[48;5;{color_num}m'

	def attr(num=0):
		if num == "reset":
			return '\33[0m'
		return f'\33[{num}m'

	def attr_list():
		webbrowser.open("https://github.com/Arozoid/BettrPy/blob/main/attr_list.txt")

	def color_list():
		webbrowser.open("https://github.com/Arozoid/BettrPy/blob/main/color_list.txt")
