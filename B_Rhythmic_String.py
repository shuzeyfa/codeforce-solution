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
    n = getInt()
    l = getIntList()
    
    visited = [False]*n
    l.sort()
    ans = 0
    
    for i in range(n):
 
        
        val = 0
        for j in range(i, n):
            if l[j]%l[i] == 0:
                val += 1
        ans = max(ans, val)
    print(n - ans)
    
             
    
for _ in range(t):
    solve()