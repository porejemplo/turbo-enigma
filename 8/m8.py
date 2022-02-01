#!/usr/bin/python3.8

import sys
import re

for line in sys.stdin:
	if re.search("^([\w\d\s\./:-]+;){7}\d+;\d+$",line):
		x=line.split(';')
		y=x[5].split('.')
		if len(y) >= 2:
			print((y[len(y)-1] +";"+ x[8]).rstrip())