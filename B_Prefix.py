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
    
    ans = l[0]
    maxx = minn = l[0]
    
    for i in range(1, n):
        

        ans = l[i] + max(abs(maxx), abs(minn))
        
        values = []
        
        values.append(l[i])
        values.append(2*maxx + l[i])
        values.append(2*minn + l[i])
        values.append(maxx + l[i])
        values.append(minn + l[i])
        
        maxx = max(values)
        minn = min(values)
        
    print(ans)   
    
        
      
             
    
for _ in range(t):
    solve()