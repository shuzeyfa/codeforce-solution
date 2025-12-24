
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
    n, m = getIntList()

    # mn[i] = max b such that [i..b] is good
    mn = [n] * (n + 2)

    for _ in range(m):
        u, v = getIntList()
        if u > v:
            u, v = v, u
        mn[u] = min(mn[u], v - 1)

    # backward propagation (YOU MISSED THIS)
    for i in range(n - 1, 0, -1):
        mn[i] = min(mn[i], mn[i + 1])

    ans = 0
    for i in range(1, n + 1):
        if mn[i] >= i:
            ans += mn[i] - i + 1

    print(ans)

                                  
    


          
            
               
     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()