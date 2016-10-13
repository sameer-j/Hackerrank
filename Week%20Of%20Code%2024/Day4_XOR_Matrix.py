#!/bin/python3


def constantList(x):
    return x and [x[0]]*len(x) == x

c,r = input().strip().split(' ')
c,r = [int(c), int(r)]
newrow = [int(i) for i in input().strip().split(' ')]
for ir in range(0, r-1):
    lastrow=newrow[:]
    for ic in range(c-1):
        newrow[ic] = lastrow[ic] ^ lastrow[ic+1]
    newrow[c-1] = lastrow[c-1] ^ lastrow[0]
    if constantList(newrow):
        break
print(*newrow)