
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
    x = getInt()
    
    for k in range(1, 100000):
        best = 0

        for c in range(k+1):
            a = k - c

            if a == 0:
                continue

            cur = c + 1

            if cur >= a:
                dec = a * (2 * cur - a + 1) // 2
            else:
                dec = cur * (cur + 1) // 2 + (a - cur)

            best = max(best, dec)

        if best >= x:
            print(k)
            return
        
                                  
    


          
            
               
     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()