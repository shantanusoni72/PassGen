import random

Chars = {"a":"@", "B":"8", "E":"3", "G":"9", "I":"1", "O":"0", "S":"$", "X":"*", "1": "L", "p": "7",
		"r":"4", "s":"5"}

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
	return encodeSimple(strpass)

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