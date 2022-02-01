#!/usr/bin/python3.8

import sys

total = 0
i = -1
cont = 0
var = []
for line in sys.stdin:
	for x, y in var:
		if line == x:
			cont+=1
			break
		i +=1
			
	if cont == 0:
		var.append([line, 0])
	var[i][1] +=1
	cont = 0
	i=0
for x, y in var:
	total += y
for x, y in var:
	print(x)
	print((y/total)*100)
