#!/usr/bin/env python3
def g(x):
    g = (1/math.sqrt(2*math.pi))*(math.exp(-x**2/2))
    return g

def f(x):
    return x

def interval(f, a, b, dx):
    N = int((b-a)/dx)
    intList =[f(a+i*dx) for i in range(0,N+1)]
    return intList
#interval(f,0,1,.1)

def integrate(i, dx):