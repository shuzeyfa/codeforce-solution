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
    
    ind = []
    val = []
    
    for i in range(n):
        if i+1 != l[i]:
            ind.append(i)
            val.append(l[i])
    
    if not val:
        print("YES")
        return
    
    val.reverse()
    
    for i in range(len(val)):
        l[ind[i]] = val[i]
    
    if sorted(l) == l:
        print("YES")
    else:
        print("NO")
        
    
             
    
for _ in range(t):
    solve()