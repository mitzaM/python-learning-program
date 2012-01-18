def flatten(q, depth):
  while depth > 0:
    a = []
    for elem in q:
      if hasattr(elem, '__iter__'):
        for num in elem:
          a.append(num)
      else:
        a.append(elem)
    depth = depth - 1
    q = a
  print q
