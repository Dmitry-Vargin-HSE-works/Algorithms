from time import time
import random
import numpy as np
from math import exp

import support

# Start data:
points_dict = support.get_data_from_file('data.txt')
n = len(points_dict.keys())
matrix = support.convert_to_dict_matrix(points_dict)
keys_list = list(points_dict.keys())
range_list = list(range(n))

best_way = tuple()
with open('result.txt') as f:
    exec('best_way = ' + f.read().strip())
print(best_way[0])
print(best_way[1])

start_way = support.get_random_way(points_dict)
start_way = [support.get_length_of_way(start_way, matrix), start_way]
global_best_ways = [start_way, ]

border = 100

# Main Program
while True:
    disturbance = 1.0
    local_best = global_best_ways[-1].copy()
    local_lengths = [local_best[0], ]
    while disturbance < 1_000_000_000:
        sep_way = global_best_ways[-1].copy()
        if disturbance < 50_000:           # 2-opt
            k1 = random.choice(range_list)
            k2 = random.choice(range_list)
            if k1 == k2:
                continue
            print(sep_way)
            print(k1, k2, end='\n\n')
            sep_way[1][k1], sep_way[1][k2] = sep_way[1][k2], sep_way[1][k1]
        else:
            k1 = random.choice(range_list)
            k2 = random.choice(range_list)
            k3 = random.choice(range_list)
            if k1 == k2 or k2 == k3 or k3 == k1:
                continue
            print(sep_way)
            print(k1, k2, k3, end='\n\n')
            sep_way[1][k1], sep_way[1][k2], sep_way[1][k3] = sep_way[1][k2], sep_way[1][k3], sep_way[1][k1]

        sep_way[0] = support.get_length_of_way(sep_way[1], matrix)
        local_lengths.append(sep_way[0])
        tmp = np.array(local_lengths)
        if sep_way[0] < local_best[0]:
            local_best = sep_way
            disturbance -= exp((1-tmp.std()/tmp.mean()))*(tmp.size-1)
        elif sep_way[0] > tmp.mean() - tmp.std():
            disturbance += exp((1-tmp.std()/tmp.mean()))*tmp.size
            # print(f'{disturbance:.2f}')
    print('next')
    global_best_ways.append(local_best)
    if local_best[0] < best_way[0]:
        best_way = local_best
        f = open('result.txt', 'w')
        print(best_way, file=f)
        print(f'New record!\n{best_way[0]}\n{best_way[1]}\n')

    if (len(global_best_ways) > 3) and (100 > support.distance(global_best_ways[-1][1], global_best_ways[-2][1])):
        global_best_ways.append(support.get_random_way(matrix))
        print('nex random')
        print(global_best_ways[-1][0], global_best_ways[-1][1], sep='\n', end='\n\n')
