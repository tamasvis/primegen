#!/usr/bin/python3

import sys,re,fileinput

k2, k3 = 977, 997

if __name__ == '__main__':
	all = list(l.rstrip('\n') for l in fileinput.input())

	p1 = list(int(re.sub('.*=0x', '', l), 16)
			for l in all  if ('P1=' in l))
	for p in p1:
		assert((p & 1) == 1)
		p2 = k2 * (p - 1) +1
		p3 = k3 * (p - 1) +1

		u = p * p2 * p3
		print(f'P1=0x{ p :x}')
		print(f'P=0x{ u :x}')

