import sys
import random
import pyfiglet
def banner():
	print("------------------------------------\n",
		pyfiglet.figlet_format("	PassGen		"),
		"\n		   Code by shaan453",
		"\n------------------------------------")
def encodeSimple(password):
	return password+str(random.randint(1,1000000))
def encodeModerate(password):
	strpass = ""
	passList = []
	for i in range(len(password)):
		passList.append(password[i]) 
	for i in range(len(passList)):
		if passList[i] in Chars:
			passList[i] = Chars.get(passList[i])
	for i in range(len(passList)):
		strpass += passList[i]
	return strpass
def readFile():
	f = open("help.txt","r")
	print(f.read())
	f.close()
def encodeHTG(password):
	strpass = ""
	passList = []
	for i in range(len(password)):
		passList.append(password[i]) 
	for i in range(len(passList)):
		if passList[i] in Chars:
			passList[i] = Chars.get(passList[i])
	for i in range(len(passList)):
		strpass += passList[i]+str(random.randint(1,99))
	return strpass
Chars = {"a":"@", "B":"8", "E":"3", "G":"9", "I":"1", "O":"0", "S":"$", "X":"*", "1": "L", "p": "7",
		"r":"4", "s":"5"}
password = sys.argv[1]
banner()
if len(sys.argv) == 2 and sys.argv[1] == "--help":
	readFile()
elif len(sys.argv) != 3:
	print("Usage: PassGen.py <string> <mode of security>")
else:
	if sys.argv[2] == "--simple":
		print("New password: ",encodeSimple(password))
	elif sys.argv[2] == "--moderate":
		print("New password: ", encodeModerate(password))
	elif sys.argv[2] == "--hard-to-guess":
		print("New password: ",encodeHTG(password))
	else: 
		readFile()