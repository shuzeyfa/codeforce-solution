import sys, os
import math, heapq
from collections import defaultdict, deque, Counter
from functools import lru_cache
from bisect import bisect_right, bisect_left

RANDOM = int.from_bytes(os.urandom(8), "big")
def getInt(): return int(sys.stdin.readline().strip())
def getStr(): return sys.stdin.readline().strip()
def getIntSeq(): return map(int, sys.stdin.readline().strip().split())
def getStrSeq(): return sys.stdin.readline().strip().split()
def getIntList(): return list(map(int, sys.stdin.readline().strip().split()))
def getStrList(): return list(sys.stdin.readline().strip().split())


t = 1
t = getInt()


 
def solve():
    n, m = getIntList()

    d = [0] * n

    for _ in range(m):
        u, v = getIntList()
        d[u - 1] += 1
        d[v - 1] += 1

    d.sort()

    if d[0] == 0:
        print("Brain Melt")
    elif d[-1] == n - 1 and d[-2] == 1:
        print(2)
    else:
        print("Many")


for _ in range(t):
    solve()
