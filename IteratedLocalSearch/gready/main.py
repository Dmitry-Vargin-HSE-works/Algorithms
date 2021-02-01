from time import time

import support
import random


def greedy_point(your_way, m: dict):
    flag = True
    lp = your_way[1][-1]
    for key in m.keys():
        if key in your_way[1]:
            continue
        if flag:
            tmp = key
            flag = False
        elif m[lp][key] < m[lp][tmp]:
            tmp = key
    return tmp


# Start data:
points_dict = support.get_data_from_file('data.txt')
pset = set(points_dict.keys())
n = len(points_dict.keys())
matrix = support.convert_to_dict_matrix(points_dict)
best = []
f = open('result.txt', 'r')
exec('best = ' + f.read().strip())
f.close()
while pset:
    r = random.choice(tuple(pset))
    pset.remove(r)
    print(f'\t{len(pset)}')
    way = [0, [r, ]]
    for i in range(1, n):
        way[1].append(greedy_point(way, matrix))
        way[0] += matrix[way[1][-1]][way[1][-2]]
    way[0] += matrix[way[1][-1]][way[1][-2]]
    if way[0] < best[0]:
        best = way
        print(f'{way[0]}\n' + ' '.join(way[1]))
        f = open('result.txt', 'w')
        print(f'{way[0]}\n' + ' '.join(way[1]), file=f)
        f.close()
