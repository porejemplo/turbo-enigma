#!/usr/bin/python3.8

import sys
busqueda1 = ""
busqueda2 = ""
busqueda3 = ""
cuenta1 = 0
cuenta2 = 0
cuenta3 = 0

for line in sys.stdin:
	line = line.rstrip()
	line = line.split(';')
	var = int(line[1])
	if var > cuenta3:
		if var > cuenta2:
			if var > cuenta1:
				cuenta3 = cuenta2
				cuenta2 = cuenta1
				cuenta1 = var
				busqueda3 = busqueda2
				busqueda2 = busqueda1
				busqueda1 = line[0]
			else:
				cuenta3 = cuenta2
				cuenta2 = var
				busqueda3 = busqueda2
				busqueda2 = line[0]
		else:
			cuenta3=var
			busqueda3 = line[0]

print(busqueda1 + ": " + str(cuenta1))
print(busqueda2 + ": " + str(cuenta2))
print(busqueda3 + ": " + str(cuenta3))