import requests
import os
import site
import time
from subprocess import Popen

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
  os.chdir(path)
  os.mkdir(name)
  print("mkdir: Created '{name}'")

def mvfile(name,directory):
  os.rename(f"{name}", f"{directory}/{os.path.basename(name)}")
  print(f"{tpainter.fg(2)}mvfile: Moved '{name}'{tpainter.fg()}")

def rmdir(self,directory):
  os.rmdir(directory)
  print(f"rmdir: Removed '{directory}'")

# Introduce you to this build script <3
print(tpainter.fg(29) + "----------------")
print("BettrPy Builder")
print(f"----------------\n{tpainter.fg(31)}Builds BettrPy for you" + tpainter.fg())
time.sleep(3)

# Check if you really want to download this
input = input("\nWould you really like to continue? [y/n] ")
if input == "y" or "Y":
  print(f"{tpainter.fg(2)}Continuing...{tpainter.fg()}")
  time.sleep(1)
else:
  exit()

# Download bettrpy and put into a directory
# This style of downloading isn't like in bettrpy
try:
  print(f"{tpainter.attr(1)}{tpainter.fg(2)}\nDownloading 'main.py'...\n{tpainter.attr()}{tpainter.fg()}")
  current_dir = os.getcwd()
  mkdir("bettrpy",current_dir)
except:
  print(f"{tpainter.fg(1)}BuildError: Something went wrong while creating directory{tpainter.fg()}")
  exit()
try:
  url = 'https://github.com/Arozoid/BettrPy/blob/main/main.py'
  download_to = f'{current_dir}/bettrpy/__main__.py'
  data = requests.get(url)
  with open(download_to, 'wb') as file:
	  file.write(data.content)
  print(f"{tpainter.fg(2)}downloader: Downloaded 'main.py'{tpainter.fg()}")
except:
  print(f"{tpainter.fg(1)}BuildError: Downloading didn't work{tpainter.fg()}")
  exit()

time.sleep(1)	
	
# Find site-packages folder and make a directory
print(f"{tpainter.attr(1)}{tpainter.fg(2)}\nMoving main.py\n{tpainter.attr()}{tpainter.fg()}")
try:
  site_folders = site.getsitepackages()
  mkdir("bettrpy",site_folders[0])
except:
  print("BuildError: For some random reason you dont have a site-packages folder..?")
  exit()
try:
  mvfile(f"{current_dir}/bettrpy/main.py","{site_folders[0]}/bettrpy")
  rmdir(f"{current_dir}/bettrpy")
except:
  print(f"{tpainter.fg(1)}BuildError: Something went wrong while transfering 'main.py'{tpainter.fg()}")
  exit()

time.sleep(1)
	
# Download all non-default dependencies
try:
  print(f"{tpainter.fg(2)}Installing wget..{tpainter.fg()}")
  Popen("pip install wget",shell=True)
except:
  print(f"{tpainter.fg(1)}BuildError: Something broke while checking dependencies{tpainter.fg()}")
  exit()

time.sleep(1)

# Yay! All done.
print(f"{tpainter.attr(1)}{tpainter.fg(29)}Yay! This build script is finished.")
exit()
