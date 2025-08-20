
import numpy as np

def func(x):
	return x**2

def SecantIter(x0,x1):
	x2 = x1 - func(x1)*( (x1-x0) / (func(x1) - func(x0)) )
	print(x0,x1,x2)
	return x1,x2

x0 = 1
x1 = 7

maxIter = 50

n=0
while n <= maxIter:
	n += 1
	[x0,x1] = SecantIter(x0,x1)

print(f"x0 = {x0}")
print(f"x1 = {x1}")

