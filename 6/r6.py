#!/usr/bin/python3.8

import sys

busqueda0 = ""
busqueda = ""
cuenta0 = 0
cuenta = 0

for line in sys.stdin:
	line = line.rstrip()
	line = line.split(';')
	if line[0] != busqueda:
		if busqueda0 != "":
			var = cuenta/cuenta0*100-100
			print(f"Desde {busqueda0} a {busqueda} a variado: var {var:.2f}%")
		busqueda0=busqueda
		busqueda = line[0]
		cuenta0 = cuenta
		cuenta = 0
	cuenta+=int(line[1])

var = cuenta/cuenta0*100-100
print(f"Desde {busqueda0} a {busqueda} a variado: var {var:.2f}%")