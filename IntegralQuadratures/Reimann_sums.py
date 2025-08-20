# code to compute the left, right, or midpoint Reimann sum of a function over a finite interval

import sys
import numpy as np

def func(y):
	y = np.array(y) # make sure this is a numpy array
	return np.sqrt(y) - y

def Reimann_sum(a,b,N,sum_type):
	x = np.linspace(a,b,N+1)
	dx = (b-a)/N
	if sum_type == "left" or sum_type == "Left":
		summ = dx*np.sum(func(x[0:-1]))
	elif sum_type == "right" or sum_type == "Right":
		summ = dx*np.sum(func(x[1:]))
	elif sum_type == "midpoint" or sum_type == "Midpoint":
		summ = dx*np.sum(func((x[0:-1] + x[1:])/2.0))
	else:
		print("Invalid sum_type. Break from script")
		sys.exit()
	print(summ)
	print(dx)

a, b = 1, 23 # endpoints of interval
N = 50 # number of rectangles

Reimann_sum(a,b,N,"left")
Reimann_sum(a,b,N,"Right")
Reimann_sum(a,b,N,"Midpoint")
Reimann_sum(a,b,N,"nothing")


