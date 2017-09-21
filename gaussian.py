#!/usr/bin/env python3
import math

import math

def g(x):
    g = (1/math.sqrt(2*math.pi))*(math.exp(-x**2/2))
    return g

def e(x):
    return math.exp(x)

def interval(f, a, b, dx):
    intList = []
    N = int((b-a)/dx)
    intList =[f(a+i*dx) for i in range(0,N+1)]
    return intList


def integrate(i, dx):
    n = len(i)
    total = 0
    for r in range(1,n-1):
        total += 2*i[r]
        total = (dx/2)*total
    return total


#if __name__ == "__main__":
    #print(interval(f,0,1,.1))

