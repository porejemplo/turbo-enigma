#!/usr/bin/python3.8

import sys
import re

for line in sys.stdin:
	if re.search("^([\w\d\s\./:-]+;){7}\d+;\d+$",line):
		x=line.split(';')
		print(x[4] +";"+ x[7][0])