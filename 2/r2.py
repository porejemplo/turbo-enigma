#!/usr/bin/python3.8

import sys
accion = ""
cuenta = 0

for line in sys.stdin:
	line = line.rstrip()
	if line != accion:
		if line != "":
			print(accion + ": " + str(cuenta))
		accion = line
		cuenta = 0
	
	cuenta+=1

print(accion + ": " + str(cuenta))
