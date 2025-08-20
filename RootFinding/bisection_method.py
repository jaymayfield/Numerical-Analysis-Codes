
# script using the bisection method to find a root of a function

import sys
import numpy as np

# function we wish to find the root of
def func(x):
	x = np.array(x) #ensure x is a numpy array
	return (x-0.3)**3

# determine the sign of a value
def sign(x):
	if x>0:
		return 1
	else:
		return 0

a, b = -2, 2	# bounds of interval
N = 1000	# number of nodes in interval
iterMAX = 1000	# max number of iterations of bisection method
TOL = 0.001	# smallest value the interval is allowed to be

x = np.linspace(a,b,N)	# array of discrete domain

# array of function
f = func(x)

# checking if a root in the interval is possible
if (func(a)<=0 and func(b)<=0) or (func(a)>=0 and func(b)>=0):
	print("Initial conditions not met")
	print("Ending script")
	sys.exit()

# Bisection method
n = 1 # used to count iterations of bisection method
while (n<=iterMAX):
	c = (a+b)/2.0 #new midpoint
	if (func(c)==0) or ((b-a)/2.0<TOL):
		print("Solution found!")
		print(f"Root = {c}")
		print(f"Number of iterations = {n}")
		print(f"f(c) = {func(c)}")
		sys.exit()
	n = n+1
	if (sign(func(a)) == sign(func(c))):
		a = c
	elif (sign(func(b)) == sign(func(c))):
		b = c
	else:
		print("what...")



