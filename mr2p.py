#!/usr/bin/python3

import sys,re,fileinput

k2, k3 = 977, 997

if __name__ == '__main__':
	all = list(l.rstrip('\n') for l in fileinput.input())

	ps = list(l  for l in all  if (('P1=' in l) or ('P3=' in l)))
	for p in ps:
		p1, p3 = 0, 0
		if 'P1=' in p:
			p1 = int(p[ p.index('=')+1 : ], 16)
			assert((p1 & 1) == 1)
			p3 = k3 * (p1 - 1) +1

		elif ('P3=' in p):
			p3 = int(p[ p.index('=')+1 : ], 16)
			assert((p3 & 1) == 1)
			p1 = (p3 -1) // k3

		else:
			assert(0)

		p2 = k2 * (p1 - 1) +1
		u  = p1 * p2 * p3
		print(f'P1=0x{ p1 :x}')
		print(f'P3=0x{ p3 :x}')
		print(f'P=0x{ u :x}')
		print(f'P.BITS={ u.bit_length() }')

