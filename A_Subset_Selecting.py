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
    
    d = Counter(l)
    count = 0
    
    for i in range(n+1):
        if d[i] == 0:
            print(i)
            return
        if d[i] >= k:
            count += (d[i] - k)
        else:
            rem = k - d[i]
            if rem > count:
                print(i)
                return
            
            count -= rem
    print(n) 
        
        
    
             
    
for _ in range(t):
    solve()