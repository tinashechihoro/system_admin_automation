#!/usr/bin/evn python3
# A system information gathering script

import subprocess

def uname():
	uname = 'uname'
	uname_argument = '-a'
	print('Gathering system information with {}  command:\n'.format(uname))
	subprocess.call([uname,uname_argument])

def diskspace():
	diskspace = 'df'
	diskspace_argument = '-h'
	print('Gathering diskspace information {} command:\n'.format(diskspace))
	subprocess.call([diskspace,diskspace_argument])

def main():
	uname()
	diskspace()

if '__name__' == '__main__':
	main()