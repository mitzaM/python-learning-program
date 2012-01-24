#!/usr/bin/env python

a = {'x': [1,2,3], 'y': 1, 'z': set([1,2,3]), 'w': 'qweqwe', 't': {'a': [1, 2]}, 'm': [1]}
b = {'x': [4,5,6], 'y': 4, 'z': set([4,2,3]), 'w': 'asdf', 't': {'a': [3, 2]}, 'm': "wer"}

def merge(obj_a, obj_b):
    """ Merges two objects with any depth

    >>> merge({}, {})
    {}

    >>> merge({'a': 1}, {})
    {'a': 1}

    >>> merge({}, {'b': 1})
    {'b': 1}

    >>> merge({'x': [1,2,3], 'y': 1, 'z': set([1,2,3]), 'w': 'qweqwe', 't': {'a': [1, 2]}, 'm': [1]}, {'x': [4,5,6], 'y': 4, 'z': set([4,2,3]), 'w': 'asdf', 't': {'a': [3, 2]}, 'm': "wer"})
    {'m': ([1], 'wer'), 't': {'a': [1, 2, 3, 2]}, 'w': 'qweqweasdf', 'y': 5, 'x': [1, 2, 3, 4, 5, 6], 'z': set([1, 2, 3, 4])}

    """
    res = {}
    for k, v in obj_a.iteritems():
	if k not in obj_b.keys():
	    res[k] = v
	else:
	    try:
		res[k] = v + obj_b[k]
	    except TypeError:
		try:
		    res[k] = v.union(obj_b[k])
		except AttributeError:
		    try:
			v.iteritems()
		    except AttributeError:
			res[k] = (v, obj_b[k])
		    else:
			res[k] = merge(v, obj_b[k])
    for k, v in obj_b.iteritems():
	if k not in obj_a.keys():
	    res[k] = v
    return res

print merge(a, b)
