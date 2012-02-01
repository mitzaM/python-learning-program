#!/usr/bin/env python

class time_slow:
    def __init__(self, *args, **kw):
	self.args = args
	self.kw = kw
	print self.kw['threshold']

    def __call__(self, func):
	print self.kw['threshold']
	func()
	print self.kw['threshold']
	return func()#*self.args, **self.kw)

@time_slow(threshold=0.05)
def test():
    return 2 + 3
