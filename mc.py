import sys
import dbm.ndbm
import os
import dulwich

HOME = os.path.expanduser("~")
DIR = HOME + "/.config-manager"

def main():
	switch = {
		'init': init,
		'clone': clone,
		'validate': validate
	}
	func = switch.get(sys.argv[1], lambda: printhelp)
	return func()

def init():
	if os.path.exists( DIR ):
		print('Folder already exists, please validate it or check ~/.config-manager')
		return 1

	os.makedirs( DIR )

	return 0

def clone():
	return 0

def validate():
	print('val-hit')
	return 0

def printhelp():
	print('Help here')
	return 1

if __name__ == '__main__':
	if len(sys.argv) == 1:
		printhelp()
	else:
		main();