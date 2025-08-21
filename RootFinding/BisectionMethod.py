
# script using the bisection method to find a root of a function

import sys
import numpy as np

##################
# Function to find the root of in a finite interval
# Input: x -- independent variable x
# Output: function value at x
##################
def func(x):
	#x = np.array(x) #ensure x is a numpy array
	return np.sin(x) - x**2/5.0

##################
# Function to determine the sign of a nonzero value
# Input: x -- value to determine the sign of
# Output: 1 for positive, 0 for negative
##################
def sign(x):
	if x>0:
		return 1
	else:
		return 0

##################
# Bisection iterative method for rootfinding
# Input: a       -- left endpoint of the finite interval
#	 b       -- right endpoint of the finite interval
#	 TOL     -- maximum size of [a,b]
#	 iterMAX -- maximum number of iterations
# Output: c -- approximate root of func(x) in [a,b]
#	  n -- number of Bisection iterations to match TOL
##################
def Bisection(a, b, TOL, iterMAX):
	# check if a root in the interval is possible
	if (func(a) <= 0 and func(b) <= 0) or (func(a) >= 0 and func(b) >= 0):
		print("Root may not be possible...")
		print("Ending script.")
		sys.exit()
	n = 0 # counter
	while (n < iterMax) and (b-a > TOL):
		n += 1
		c = (a+b)/2.0 # new midpoint
		if (sign(func(a)) == sign(func(c))):
			a = c
		elif (sign(func(b)) == sign(func(b))):
			b = c
		else:
			print("Problem encountered...")
			print("Ending script.")
			sys.exit()
	return c, n

a, b = 0.1, 50	# bounds of interval
iterMax = 50	# max number of iterations of bisection method
TOL = 1e-7	# smallest value the interval is allowed to be

[root, iters] = Bisection(a, b, TOL, iterMax)

print(f"Approximate root = {root}")
print(f"Number of iterations: {iters}")
