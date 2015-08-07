import sys

def main():
	return 0

def printhelp():
	print 'Help here'
	return 1

if __name__ == '__main__':
	print sys.argv
	if len(sys.argv) == 1:
		printhelp()
	else:
		main();