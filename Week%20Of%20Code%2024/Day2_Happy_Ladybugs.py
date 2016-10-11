#!/bin/python3
"""
https://www.hackerrank.com/contests/w24/challenges/happy-ladybugs
"""
import sys
from itertools import groupby

Q = int(input().strip())
for a0 in range(Q):
    n = int(input().strip())
    b = list(input().strip())
    result = []
    uniq_b = set(b)
    if '_' not in uniq_b:
        for x, y in groupby(b):
            if len(list(y))>=2:
                result.append(True)
            else:
                result.append(False)
    else:
        for elm in uniq_b:
            if elm is not '_' and b.count(elm) > 1:
                result.append(True)
            elif elm is not '_' and b.count(elm) == 1:
                result.append(False)
    if False in result:
        print('NO')
    else:
        print('YES')
