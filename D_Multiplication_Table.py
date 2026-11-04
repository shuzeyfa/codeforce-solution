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


def solve():
    n, m, k = getIntList()
    if n > m:
        n, m = m, n
    
    def count(x):
        res = 0
        for i in range(1, n + 1):
            res += min(m, x // i)
            if res >= k:
                return res
        return res
    
    left, right = 1, n * m
    while left < right:
        mid = (left + right) // 2
        if count(mid) >= k:
            right = mid
        else:
            left = mid + 1
    print(left)


t = 1
# t = getInt()
for _ in range(t):
    solve()