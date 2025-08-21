
# code to use Newton's method to find the root of a function

import numpy as np

##################
# Function of which we wish to find the root of
# Input: x -- any element in the finite interval
# Output: the function evaluated at input x
##################
def func(x):
	return np.sin(x) - x**2/5.0

##################
# Derivative of the function from func(x)
# Input: x -- any element in the finite interval
# Output: the derivative of the func(x) at the input x
##################
def dfunc(x):
	return np.cos(x) - (2.0/5.0)*x

##################
# Newton's iterative method
# Input: x0      -- initial guess to the root
#	 matIter -- the maximum number of allowed Newton Iterations
#	 TOL     -- tolerance between func(x) and 0
# Output: x0 -- Approximate root of the function from func(x) in the given interval
#	  n  -- number of iterations to match TOL	  
##################
def Newton(x0, maxIter, TOL):
	n = 0 # counter
	x1 = 0.0
	while (n < maxIter) and abs(func(x0)) > TOL:
		n += 1
		x1 = x0 - func(x0)/dfunc(x0)
		x0 = x1
	return x0, n

#initial guess
x0 = 5
# max iterations
maxIter = 1e2
# tolerance of the approximate root
TOL = 1e-9

[x0, iters] = Newton(x0, maxIter, TOL)

print(f"Root = {x0}")
print(f"Number of iterations: {iters}")
