import sys
import shelve
import os
import dulwich

HOME = os.path.expanduser("~")
DIR = HOME + "/.cm/"

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
		print('Folder already exists, please validate it or check ~/.cm')
		return 1

	os.makedirs( DIR )
	db = shelve.open(DIR + "cnf.db",'n',0)
	test = {}
	test["rnd"] = ["!","@"]
	test["rand"] = ["#","$"]
	db["test"]=["testing","ttesting"]
	db["bla"]=test
	db.close()


	return 0

def clone():
	return 0

def validate():
	return 0

def printhelp():
	print('Help here')
	return 1

if __name__ == '__main__':
	if len(sys.argv) == 1:
		printhelp()
	else:
		main();