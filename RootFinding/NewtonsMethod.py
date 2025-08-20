
# code to use Newton's method to find the root of a function

import numpy as np

def func(x):
	return np.exp(x) - 2.0

def dfunc(x):
	return np.exp(x)

def NewtonIter(x0):
	return x0 - func(x0)/dfunc(x0)

#initial guess
x0 = 5

maxIter = 50

n = 0 #counter
while n <= maxIter:
	n +=1
	x0 = NewtonIter(x0)

print(f"Root = {x0}")
print(np.log(2))

