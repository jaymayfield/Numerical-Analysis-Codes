# code to compute the Trapezoid sum of a function over a finite interval

import sys
import numpy as np

def func(y):
	y = np.array(y) # make sure this is a numpy array
	return np.sqrt(y) - y

def Simp_sum(a,b,N):
	if N % 2 != 0:
		print("Simpsons Rule requires N be even!")
		print("Leaving script...")
		sys.exit()
	x = np.linspace(a,b,N+1)
	dx = (b-a)/N

	# add the endpoints
	summ = func(x[0]) + func(x[N])

	# sum of odd interior nodes
	summ += 4*np.sum(func(x[1:N:2]))

	# sum of even interior nodes
	summ += 2*np.sum(func(x[2:N-1:2]))

	summ *= dx/3.0

#	summ = 0.0
#	for i in range(0,N,2):
#		summ = summ + func(x[i]) + 4*func((x[i]+x[i+1])/2.0) + func(x[i+1])
#	summ = dx/3.0*summ
	print(dx)
	print(summ)

a, b = 1, 23 # endpoints of interval
N = 50 # number of rectangles
#n = N + 1 # number of nodes in mesh


# x = np.linspace(a,b,n)

Simp_sum(a,b,N)

