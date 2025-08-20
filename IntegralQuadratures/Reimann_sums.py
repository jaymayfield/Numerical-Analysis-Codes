# code to compute the left, right, or midpoint Reimann sum of a function over a finite interval

import sys
import numpy as np

def func(y):
	y = np.array(y) # make sure this is a numpy array
	return np.sqrt(y) - y

def Reimann_sum(a,b,x,N,sum_type):#left first
	dx = (b-a)/N
	summ = 0.0
	if sum_type == "left" or sum_type == "Left":
		for i in range(0,N):
			summ = summ + func(x[i])
	elif sum_type == "right" or sum_type == "Right":
		for i in range(1,N+1):
			summ = summ + func(x[i])
	elif sum_type == "midpoint" or sum_type == "Midpoint":
		for i in range(0,N):
			summ = summ + func((x[i]+x[i+1])/2.0)
	else:
		print("Invalid sum_type. Break from script")
		sys.exit()
	summ = dx*summ
	print(summ)
	print(dx)

a, b = 1, 23 # endpoints of interval
N = 50 # number of rectangles
n = N + 1 # number of nodes in mesh
#sum_type = "left"

x = np.linspace(a,b,n)

Reimann_sum(a,b,x,N,"left")
Reimann_sum(a,b,x,N,"Right")
Reimann_sum(a,b,x,N,"Midpoint")
Reimann_sum(a,b,x,N,"nothing")


