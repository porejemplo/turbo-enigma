#!/usr/bin/python3.8

import sys

dominio = ""
cont = 0

for line in sys.stdin:
	line = line.rstrip()
	line = line.split(',')

	if line[0] != dominio:
		if dominio != "":
			print(dominio + ": " + str(cont))
		dominio = line[0]
		cont = 0

	if line[2] == "GET":
		cont += int(line[1])
	elif line[2] == "POST":
		cont -= int(line[1])

print(dominio + ": " + str(cont))