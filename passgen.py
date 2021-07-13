import random
import sys

sys.path.insert(0, '/home/shaan/Projects/PassGen')

from build.file import *
from build.modes import *

password = sys.argv[1]
banner()

if len(sys.argv) == 2 and sys.argv[1] == "--help":
	readFile()
elif len(sys.argv) != 3:
	print("[*] Usage: PassGen.py <string> <mode-of-security>")
else:
	if sys.argv[2] == "--simple":
		print("[*] New password: ",encodeSimple(password))
	elif sys.argv[2] == "--moderate":
		print("[*] New password: ", encodeModerate(password))
	elif sys.argv[2] == "--hard-to-guess":
		print("[*] New password: ",encodeHTG(password))
	else: 
		readFile()
