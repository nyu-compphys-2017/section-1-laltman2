# This is a python file! The '#' character indicates that the following line is a comment.

from __future__ import division
import numpy as np

# The following is an example for how to define a function in Python
# def tells the compiler that hello_world is the name of a function
# this implementation of hello_world takes a string as an argument,
# which has default value of the empty string. If the user calls 
# hello_world() without an argument, then the compiler uses ''
# as the default value of the argument.
def hello_world(name=''):
    print "hello world!"
    print name
    return

def right_reimann_sum(fn, n, a, b):
    width = (b-a)/n
    xvals = np.arange(a+width,b+width,width)
    yvals = fn(xvals)
    rsum = np.sum(width*yvals)
    return rsum

#Implement the Riemann Sum approximation for integrals.
