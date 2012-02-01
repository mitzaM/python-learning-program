#!/usr/bin/env python

def flatten(list_a, max_depth):
  while max_depth > 0:
    a = []
    for elem in list_a:
      if hasattr(elem, '__iter__'):
        for num in elem:
          a.append(num)
      else:
        a.append(elem)
    max_depth = max_depth - 1
    list_a = a
  print list_a

q = [0, [1, 2], [3, [4, 5]], [[[6], 7, [8]], 9]]
flatten(q, 0)
flatten(q, 1)
flatten(q, 2)
flatten(q, 3)
