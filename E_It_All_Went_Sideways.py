
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
    
    used = False
    
    for i in range(n-2, -1, -1):
        if l[i] < l[i+1]:
            continue
        
        if not used:
            used = True
            l[i+1] -= 1
        val = l[i] - l[i+1]
        l[i] -= val
        ans += val
    
    print(ans)
        
    
    
    
    
            
               
     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()