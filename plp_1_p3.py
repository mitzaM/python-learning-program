#! /usr//bin/env python

def _sort_list(l):
    """
        Sorts a list of (key, value) pairs
    """

    for i in range(len(l) - 1):
        for j in range(i + 1, len(l)):
            if (l[i][0] > l[j][0]):
                l[i], l[j] = l[j], l[i]
    return l


def _compare_dict(dict_a, dict_b):
    """
	Compares two dictionaries and returns >0 if dict_a > dict_b
					       0 if dict_a = dict_b
					      <0 if dict_a < dict_b
    """

    list_a = _sort_list(dict_a.items())
    list_b = _sort_list(dict_b.items())
    i =  t = 0

    while i < len(list_a) and i < len(list_b) and t == 0:
	t = list_a[i][1] - list_b[i][1]
	i += 1
    if (i == len(list_a)): t = -1
    if (i == len(list_b)): t = 1
    return t;


def sort_dict(file):
    """
	Reads a list of dictionaries from 'file' and sorts them
    """

    f = open(file)
    dict_list = []
    i = 0
    dict_list.append({})

    for line in f:
	if (line == '\n'):
	    i += 1
	    dict_list.append({})
	else:
	    dict_list[i][line[0]] = int(line[2])
    f.close()

    idx_list = range(len(dict_list));
    for i in range(len(dict_list) - 1):
	for j in range(i + 1, len(dict_list)):
	    if (_compare_dict(dict_list[i], dict_list[j]) > 0):
		idx_list[i], idx_list[j] = idx_list[j], idx_list[i]

    f = open('result', 'r+')
    for i in idx_list:
	f.write(str(i))
	f.write(' ')
    f.write('\n')
    f.close()

sort_dict('file')
