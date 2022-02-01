#!/usr/bin/python3.8

import sys
contador_gets = 0

for line in sys.stdin:
	contador_gets+=1

print("GET;" + str(contador_gets))