# code to compute the Trapezoid sum of a function over a finite interval

import sys
import numpy as np

def func(y):
	y = np.array(y) # make sure this is a numpy array
	return np.sqrt(y) - y

def Trap_sum(a,b,N):
	x = np.linspace(a,b,N+1)
	dx = (b-a)/N
	
	summ = func(x[0]) + func(x[-1])
	summ += 2*np.sum(func(x[1:-1]))
	summ *= dx/2
	print(dx)
	print(summ)

a, b = 1, 23 # endpoints of interval
N = 50 # number of rectangles

Trap_sum(a,b,N)

