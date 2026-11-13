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
    n, k, a, b = getIntList()
    
    l = []
    
    for i in range(n):
        left, right = getIntList()
        l.append((left, right))
    
    first = float('inf')
    sec = float('inf')
    
    ans = abs( l[a-1][0] - l[b-1][0] ) + abs( l[a-1][1] - l[b-1][1] )
    
    for i in range(k):
        val = abs(l[a-1][0] - l[i][0]) + abs(l[a-1][1] - l[i][1])
        first = min(first, val)
        
        val = abs(l[b-1][0] - l[i][0]) + abs(l[b-1][1] - l[i][1])
        sec = min(sec, val)
    print(min(ans, sec+first))
        
    
             
    
for _ in range(t):
    solve()