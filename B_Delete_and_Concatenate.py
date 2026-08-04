import sys, os
import math
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
    n, c = getIntList()
    l = getIntList()

    total = sum(l)
    l.sort()

    prefix = 0
    best = 0

    for k in range(1, n // 2 + 1):
        prefix += l[k - 1]
        best = max(best, k * c - prefix)

    print(total - n * c + best)
    
    
    
    
    
    

for _ in range(t):
    solve()