#!/bin/python3

import math
import os
import random
import re
import sys


def solution(N, Q, Queries):
    # Write your code here
    bitmask = [False] * N
    # print(bitmask)
    ans = 0
    for i in range(Q):
        type_of_query, l, r = Queries[i]
        if type_of_query == 0:
            # update
            for j in range(l, r+1):
                bitmask[j] = not bitmask[j]
        else:
            # query
            # s = sum(bitmask[l: r+1])
            # print(bitmask[l: r+1], sum(bitmask[l: r+1]))
            ans += sum(bitmask[l: r+1])
    return ans % 1000000007


if __name__ == '__main__':
    N = int(input())
    Q = int(input())
    Queries = []
    for i in range(Q):
        Queries.append([int(i) for i in input().split()])
    result = solution(N, Q, Queries)
    print(result)

"""
Testcase

5
4
0 1 3
1 1 2
0 0 4
1 3 4

Output:
3
"""
