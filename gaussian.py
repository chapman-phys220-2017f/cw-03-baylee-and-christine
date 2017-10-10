#!/usr/bin/env python3
import math
                                ### Don't forget docstrings!
import math                     ### Extra math import here

def g(x):
    g = (1/math.sqrt(2*math.pi))*(math.exp(-x**2/2))
    return g

def e(x):                       ### This function just wraps math.exp. Better to just use math.exp directly.
    return math.exp(x)

def interval(f, a, b, dx):
    intList = []
    N = int((b-a)/dx)
    intList =[f(a+i*dx) for i in range(0,N+1)]
    return intList


def integrate(i, dx):          ### Use docstrings to explain what algorithm you are using here. Trapezoid rule?
    n = len(i)
    total = i[0]+i[n-1]
    for r in range(1,n-1):
        total += 2*i[r]
    total = (dx/2)*total
    return total


#if __name__ == "__main__":      ### This would fail if uncommented, since f is not defined.
    #print(interval(f,0,1,.1))

