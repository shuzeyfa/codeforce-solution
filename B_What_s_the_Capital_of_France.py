
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


t = getInt()


def solve():
    n = getInt()
    l = getIntList()

    l.sort()
    maxx = l[-1]
    minn = l[0]
    ans = maxx

    for ind in range(30, -1, -1):
        if ans & (1 << ind):
            continue

        
        if maxx  < (1 << ind):
            continue

        if minn & (1 << ind):
            ans |= (1 << ind)
            continue

        time = 1 << (ind + 1)
        val = time - 1
        final = (minn & ~val) | (1 << ind)

        if final < minn:
            final += time

        if final <= maxx:
            ans |= (1 << ind)

    print(ans)


for _ in range(t):
    solve()
