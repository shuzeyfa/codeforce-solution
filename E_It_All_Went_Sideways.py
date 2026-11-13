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
    
    ans = 0
    
    minn = [l[-1]]
    
    for i in range(n-2, -1, -1):
        val = min(minn[-1], l[i])
        minn.append(val)
        
    minn.reverse()    
    longest = 0
    
    ans = sum(l) - sum(minn)
    
    ind = 0
    
    while ind < n:
        
        i = ind
        while i < n and minn[i] == minn[ind]:
            i += 1
        longest = max(longest, i - ind)
        ind = i
        
    print(ans + longest - 1)
    
    
        
        
        
    
        
    
    
    
    
            
               
     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()