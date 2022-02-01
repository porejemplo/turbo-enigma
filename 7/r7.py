#!/usr/bin/python3.8

import sys

dominio1 = ""
dominio2 = ""
dominio3 = ""
cuenta1 = 0
cuenta2 = 0
cuenta3 = 0

for line in sys.stdin:
	line = line.rstrip()
	line = line.split(',')
	var = int(line[0])
	if var > cuenta3:
		if var > cuenta2:
			if var > cuenta1:
				cuenta3 = cuenta2
				cuenta2 = cuenta1
				cuenta1 = var
				dominio3 = dominio2
				dominio2 = dominio1
				dominio1 = line[1]
			else:
				cuenta3 = cuenta2
				cuenta2 = var
				dominio3 = dominio2
				dominio2 = line[1]
		else:
			cuenta3=var
			dominio3 = line[1]

print(dominio1 + ": " + str(cuenta1))
print(dominio2 + ": " + str(cuenta2))
print(dominio3 + ": " + str(cuenta3))