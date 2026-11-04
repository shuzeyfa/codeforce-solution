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
# t = getInt()


          
def solve():
    n, m = getIntList()
    
    par = [0]*n
    
    nextAlive = [i for i in range(n+1)]
    # print(nextAlive)
    
    def find(val):
        
        while nextAlive[val] != val:
            nextAlive[val] = nextAlive[nextAlive[val]]
            val = nextAlive[val]
        
        return nextAlive[val]
    
    for i in range(m):
        
        left, right, x = getIntList()
        
        j = find(left-1) 
        
        while j < right:
            
            if j+1 == x:
                j = find(j+1)
                continue
            
            par[j] = x
            
            nextAlive[j] = find(j+1)
            
            j = nextAlive[j]
            
        
    print(*par)
             
    
for _ in range(t):
    solve()