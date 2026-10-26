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
    
    if k >= 3:
        print(0)
        return
    
    l.sort()
    # print(l) 
    for i in range(1, n):
        l.append(l[i] - l[i-1])
    k -= 1
    
    if k == 1:
        l.sort()
        for i in range(1, len(l)):
            l.append(l[i] - l[i-1])
    
    ans = float("inf")
    l.sort()
    
    for i in range(len(l)):
        ans = min(ans, l[i])
    
    print(ans)
    # print(l)
        
    
             
    
for _ in range(t):
    solve()