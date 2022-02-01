#!/usr/bin/python3.8

import sys

tipo = ""

for line in sys.stdin:
	line = line.rstrip()
	if line != tipo:
		if tipo != "":
			print(tipo)
		tipo = line		

print(tipo)