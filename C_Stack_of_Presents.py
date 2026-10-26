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
    n, k = getIntList()
    l = getIntList()
    b = getIntList()
    
    d = defaultdict(int)
    
    for i in range(n):
        d[l[i]] = i + 1
    # print(d)
    
    
    maxx = -1
    ans = 0
    # print(d)
    removed = 0
    for i in b:
        ind = d[i]
        # print(ind, i, maxx)
        
        if ind <= maxx:
            ans += 1
        else:
            k = max(0, ind - 1 - removed)
            ans += (2*(k) + 1)
            maxx = max(maxx, ind)
        removed += 1
    print(ans)
        
        
    
             
    
for _ in range(t):
    solve()