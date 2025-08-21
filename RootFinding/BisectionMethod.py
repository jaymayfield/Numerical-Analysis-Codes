
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

# one iteration of the bisection method
def bisection(a, b, TOL, n):
	c = (a+b)/2.0 # new midpoint
	if (func(c)==0 or ((b-a)/2.0)<TOL): #solution found
		print("Solution found!")
		print(f"Root = {c}")
		print(f"f(c) = {func(c)}")
		print(f"Number of iterations = {n-1}")
		sys.exit()
	
	if(sign(func(a)) == sign(func(c))):
		a = c
	elif(sign(func(b)) == sign(func(c))):
		b = c
	else:
		print("what...")
		sys.exit()
	return a,b,c

a, b = -2, 2	# bounds of interval
iterMAX = 5	# max number of iterations of bisection method
TOL = 0.001	# smallest value the interval is allowed to be


# checking if a root in the interval is possible
if (func(a)<=0 and func(b)<=0) or (func(a)>=0 and func(b)>=0):
	print("Initial conditions not met")
	print("Ending script")
	sys.exit()

# Bisection method
n = 0 # used to count iterations of bisection method
while (n<=iterMAX):
	n = n+1
	[a,b,c] = bisection(a,b,TOL,n)

if (n > iterMAX):
	print("Maximum iterations obtained.")
	print(f"Approximate root = {c}")
	sys.exit()


