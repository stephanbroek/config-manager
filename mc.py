import sys
import csv
import os

HOME = os.path.expanduser("~")

def main():
	switch = {
		'init': init,
		'validate': validate
	}
	func = switch.get(sys.argv[1], lambda: printhelp)
	return func()

def init():
	if os.path.exists( HOME + "/.config-manager/test"):
		print 'Folder already exists, please validate it or check ~/.config-manager'
		return 1

	os.makedirs(HOME + "/.config-manager")

	#with open('config.csv')
	return 0

def validate():
	print 'val-hit'
	return 0

def printhelp():
	print 'Help here'
	return 1

if __name__ == '__main__':
	if len(sys.argv) == 1:
		printhelp()
	else:
		main();