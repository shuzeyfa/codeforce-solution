
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
    n, x, m = getIntList()

    get = False
    left, right = -1, -1

    for i in range(m):
        left2, right2 = getIntList()

        if left2 <= x <= right2 and not get:
            get = True
            left, right = left2, right2
            continue

        if left2 > right or right2 < left:
            continue

        left, right = min(left, left2), max(right,  right2)

    print(right - left + 1)     
                                  
    


          
            
               
     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()