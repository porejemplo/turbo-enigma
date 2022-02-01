#!/usr/bin/python3.8

import sys
busqueda = ""
cuenta = 0

for line in sys.stdin:
	line = line.rstrip()
	
	if line != busqueda:
		if busqueda != "":
			print(busqueda + "XX : " + str(cuenta))
		busqueda = line
		cuenta = 0

	cuenta+=1

print(busqueda + "XX : " + str(cuenta))    