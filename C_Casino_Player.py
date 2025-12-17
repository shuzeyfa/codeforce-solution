
import sys, os
import math
from collections import defaultdict, deque, Counter
from functools import lru_cache
from bisect import bisect_right, bisect_left
from heapq import heappop, heappush
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

    l = []

    for i in range(n):
        left, right, real = getIntList()
        l.append((left, right, real))

    l.sort(key=lambda x:(x[0], -x[1], -x[2]))

    ans = k

    for i in range(n):
        left, right, real = l[i]
        if left <= ans <= right:
            ans = max(real, ans)
        
    print(ans)

    
    


          
            
               
     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()