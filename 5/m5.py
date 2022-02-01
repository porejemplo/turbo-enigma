#!/usr/bin/python3.8

import sys
import re

for line in sys.stdin:
	if re.search("^([\w\d\s\./:-]+;){7}\d+;\d+$",line):
		x=line.split(';')
		z = x[3].split(' ')
		z = z[1].split(':')
		if z[0] == "00":
			if x[7] == "404":
				y = x[5].split('.')
				if len(y) == 2:
					print(y[1])


