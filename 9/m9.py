#!/usr/bin/python3.8

import sys
import re

for line in sys.stdin:
	if re.search("^([\w\d\s\./:-]+;){7}\d+;\d+$",line):
		x=line.split(';')
		if x[4] == "GET" or x[4] == "POST":
			print(f"{x[0].rstrip()},{x[8].rstrip()},{x[4].rstrip()}")