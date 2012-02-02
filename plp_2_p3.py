#!/usr/bin/env python

from time import time
from time import sleep
import functools

def time_slow(f=None, threshold=0.01):
    def decorated(f):
	@functools.wraps(f)
	def wrapper(*args, **kw):
	    start = time()
	    try:
		ret = f(*args, **kw)
	    finally:
		duration = time() - start
		if duration > threshold:
		    print '{0} took {1} seconds'.format(f.__name__, duration)
	    return ret
	return wrapper
    if f is not None:
	return decorated(f)
    return decorated

@time_slow(threshold=0.05)
def test():
    sleep(0.07)

@time_slow
def test2():
    pass

test()
test2()
