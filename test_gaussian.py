#!/usr/bin/env python3

"""Gaussian Module Unit Tests"""

import nose
import math
import gaussian

def test_g():
    # Pre-computed correct value of g(0)
    actual = 1.0/math.sqrt(2*math.pi)
    # Testing
    trial = gaussian.g(0)
    # Debug messages like this are only printed if the test fails
    print("Testing g(0): ",actual," ?= ",trial)
    # an assert command is the actual test
    # for floats, be sure to use assert_almost_equal instead (here to 4 digits)
    nose.tools.assert_almost_equal(actual, trial, 4)

def test_interval():
    # Pre-computed correct value of interval(f,0,1,.2)
    actual = [gaussian.g(0), gaussian.g(.5), gaussian.g(1)]
    # Testing implementation
    trial = gaussian.interval(gaussian.g,0,1,.5)
    # Debug messages
    print("Testing interval(f,0,1,0.5): ",actual," ?= ",trial)
    for r in range(0,2):
        nose.tools.assert_almost_equal(actual[r], trial[r], 4)

def test_integrate():
    # Pre-computed correct value of the integral
    actual = (1/2)*(gaussian.g(-1)+(2*gaussian.g(0))+(2*gaussian.g(1))+gaussian.g(2))
    # Testing
    trial = gaussian.integrate(gaussian.interval(gaussian.g,-1,2,1),1)
    # Debug
    print("Testing integral from -1 to 1: ",actual," ?= ",trial)
    #assert
    nose.tools.assert_almost_equal(actual, trial)
    
def test_gauss_norm():
    # Pre-computed correct value of integral(i,dx)
    actual = 1.00000
    # Testing
    trial = gaussian.integrate(gaussian.interval(gaussian.g,-20,20,.1),.1)
    #Debug
    print("Testing integral of normalized Gaussian function from -20 to 20: ",actual," ?= ",trial)
    #assert
    nose.tools.assert_almost_equal(actual, trial, 4)
    
    
    
    
    
    