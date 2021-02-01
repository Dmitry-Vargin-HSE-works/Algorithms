from itertools import permutations
from math import sqrt, factorial, pow
import random


def get_data_from_file(file_name: str) -> dict:
    f = open(file_name)
    n = f.readline()
    result = {}
    for line in f.readlines():
        tmp = line.split()
        result[tmp[0]] = (int(tmp[1]), int(tmp[2]))
    return result


def convert_to_dict_matrix(my_dict: dict) -> dict:
    result = {}
    for k1, v1 in my_dict.items():
        result[k1] = {}
        for k2, v2 in my_dict.items():
            result[k1][k2] = sqrt(pow(v1[0] - v2[0], 2) + pow(v1[1] - v2[1], 2))
        del result[k1][k1]
    return result


def get_length_of_way(way, values: dict) -> float:
    result = 0
    for i in range(len(way)-1):
        result += values[way[i]][way[i+1]]
    return result


def get_random_way(table: dict) -> list:
    n = len(table.keys())
    tmp_keys = list(table.keys())
    tmp_way = []
    for i in range(n):
        tmp_way.append(tmp_keys.pop(random.randrange(n-i)))
    tmp_way.append(tmp_way[0])
    return tmp_way


def distance(a, b):
    """Calculates the Levenshtein distance between a and b."""
    n, m = len(a), len(b)
    if n > m:
        # Make sure n <= m, to use O(min(n, m)) space
        a, b = b, a
        n, m = m, n

    current_row = range(n + 1)  # Keep current and previous row, not entire matrix
    for i in range(1, m + 1):
        previous_row, current_row = current_row, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
            if a[j - 1] != b[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)

    return current_row[n]

