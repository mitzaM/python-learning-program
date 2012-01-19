#!/usr/bin/env python

a = {'x': [1,2,3], 'y': 1, 'z': set([1,2,3]), 'w': 'qweqwe', 't': {'a': [1, 2]}, 'm': [1]}
b = {'x': [4,5,6], 'y': 4, 'z': set([4,2,3]), 'w': 'asdf', 't': {'a': [3, 2]}, 'm': "wer"}

def merge(a, b):
  res = {}
  for k, v in a.iteritems():
    if k not in b.keys():
      res[k] = v
    elif type(v) != type(b[k]):
      res[k] = (v, b[k])
    elif type(v) == type(b[k]) and type(v) == set:
      res[k] = v.union(b[k])
    elif type(v) == type(b[k]) and type(v) == dict:
      res[k] = merge(v, b[k])
    else:
      res[k] = v + b[k]
  return res

print merge(a, b)
