
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


t = 1
t = getInt()

   
          
def solve():
    n = getInt()
    l = getIntList()
    
    x = y = -1
    first = False
    
    for i in range(2*n):
        if l[i] == 0:
            if not first:
                x = i
                first = True
            else:
                y = i
                break
    
    def expand(left, right):
        
        d = defaultdict(int)
        mex = 0
        
        while left >= 0 and right < 2*n and l[left] == l[right]:
            
            d[l[left]] += 1
            
            while d[mex] > 0:
                mex += 1
            
            left -= 1
            right += 1
        return mex
            
    
    
    
    print(max(  expand(x, x)    , expand(y, y)  , expand(((x + y) // 2), ((x + y + 1) // 2))  ))
    
    
            
               
     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()

