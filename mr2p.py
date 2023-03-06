#!/usr/bin/python3

import sys,re,fileinput

if __name__ == '__main__':
	all = list(l.rstrip('\n') for l in fileinput.input())

	p1 = list(int(re.sub('.*=0x', '', l), 16)
			for l in all  if ('P1=' in l))

	print(p1)

