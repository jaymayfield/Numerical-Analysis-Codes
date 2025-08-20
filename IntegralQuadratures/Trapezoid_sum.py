# code to compute the Trapezoid sum of a function over a finite interval

import sys
import numpy as np

def func(y):
	y = np.array(y) # make sure this is a numpy array
	return np.sqrt(y) - y

def Trap_sum(a,b,x,N):
	dx = (b-a)/N
	summ = 0.0
	for i in range(0,N):
		summ = summ + (func(x[i]) + func(x[i+1]))/2.0
	summ = dx*summ
	print(dx)
	print(summ)

a, b = 1, 23 # endpoints of interval
N = 50 # number of rectangles
n = N + 1 # number of nodes in mesh


x = np.linspace(a,b,n)

Trap_sum(a,b,x,N)

