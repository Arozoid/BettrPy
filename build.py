# Make sure to run this as super user!

#!/usr/bin/python
import requests
import os
import site
import time
from subprocess import Popen, call
import threading

# Creates ONLY the functions we need from bettrpy
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

def mkdir(name,path):
  mkdir = os.path.join(path,name)
  os.mkdir(mkdir)
  print(f"{tpainter.fg(10)}mkdir: Created '{name}'{tpainter.fg()}")

def mvfile(name,directory):
  os.rename(f"{name}", f"{directory}/{os.path.basename(name)}")
  print(f"{tpainter.fg(10)}mvfile: Moved '{name}'{tpainter.fg()}")

def rmdir(directory):
  os.rmdir(directory)
  print(f"{tpainter.fg(9)}rmdir: Removed '{directory}'{tpainter.fg()}")

# Introduce you to this build script <3
print(tpainter.fg(29) + tpainter.attr(1) + "----------------")
print("BettrPy Builder")
print(f"----------------\n{tpainter.fg(31)}Builds BettrPy for you" + tpainter.fg() + tpainter.attr())
time.sleep(3)

# Check if you really want to download this
_input = input(f"\n{tpainter.fg(11)}{tpainter.attr(1)}Would you really like to continue? [y/n] {tpainter.attr()}")
if _input == "y":
  print(f"{tpainter.fg(10)}Continuing...{tpainter.fg()}")
  time.sleep(1)
elif _input == "Y":
  print(f"{tpainter.fg(10)}Continuing...{tpainter.fg()}")
else:
  exit()

# Download bettrpy and put into a directory
# This style of downloading isn't like in bettrpy
try:
  print(f"{tpainter.attr(1)}{tpainter.fg(10)}\nDownloading 'main.py'...\n{tpainter.attr()}{tpainter.fg()}")
  current_dir = os.getcwd()
  mkdir("bettrpy",current_dir)
except:
  print(f"{tpainter.fg(1)}BuildError: Something went wrong while creating directory{tpainter.fg()}")
  exit()
try:
  url = 'https://pastebin.com/raw/ctcwXX1y'
  download_to = f'{current_dir}/bettrpy/bettrpy.py'
  data = requests.get(url)
  with open(download_to, 'wb') as file:
	  file.write(data.content)
  print(f"{tpainter.fg(10)}downloader: Downloaded 'main.py'{tpainter.fg()}")
except:
  print(f"{tpainter.fg(1)}BuildError: Downloading didn't work{tpainter.fg()}")
  exit()

time.sleep(1)

# Find site-packages folder and make a directory
print(f"{tpainter.attr(1)}{tpainter.fg(10)}\nMoving main.py\n{tpainter.attr()}{tpainter.fg()}")
try:
  site_folders = site.getsitepackages()
except:
 print("BuildError: For some random reason you dont have a site-packages folder..?")
 exit()
try:
  mvfile(f"{current_dir}/bettrpy/bettrpy.py",f"{site_folders[0]}")
  rmdir(f"{current_dir}/bettrpy")
except PermissionError:
  print(f"{tpainter.fg(1)}BuildError: You aren't running this as root!{tpainter.fg()}")
  exit()

time.sleep(1)

# Download all non-default dependencies
print(f"\n{tpainter.fg(10)}{tpainter.attr(1)}Downloading dependencies{tpainter.attr()}{tpainter.fg()}\n")
try:
  print(f"{tpainter.fg(2)}Installing wget..\n")
  call("pip install wget",shell=True)
  print(f"\n{tpainter.attr(1)}Finished dependencies!{tpainter.attr()}\n")
except:
  print(f"{tpainter.fg(1)}BuildError: Something broke while checking dependencies{tpainter.fg()}")
  exit()

time.sleep(1)

# Yay! All done.
print(f"{tpainter.attr(1)}{tpainter.fg(29)}Yay! This build script is finished.\n{tpainter.attr()}{tpainter.fg()}")
exit()
