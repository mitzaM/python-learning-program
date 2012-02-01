#!/usr/bin/env python

a = {'a': [1], 'b': 2}

def is_hashable(object):
    try:
	hash(object)
    except TypeError:
	return False
    return True

def swap_dict(object):
    print object
    for i in object.itervalues():
	if not is_hashable(i):
	    print 'Swap is not possible'
	    return
    result = dict((v, k) for k, v in a.iteritems())
    print result

swap_dict(a)
