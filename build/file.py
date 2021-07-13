def banner():
    print("-"*70,
		"\n",
		"[*] Starting PassGen 2021.5.3... \n",
		"[*] Code by @shaan453 \n",
		"-"*70)

def readFile():
	f = open("help.txt","r")
	print(f.read())
	f.close()