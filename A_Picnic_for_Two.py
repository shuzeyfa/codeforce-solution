
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
    left, straw, blue = getIntList()
    
    first = [0]
    sec = [0]
    
    cur = 1
    while True:
        
        val = (cur*straw) % left
        if val in first:
            break
        first.append(val)
        cur += 1
    
    cur = 1
    while True:
        
        val = (cur*blue) % left
        if val in sec:
            break
        sec.append(val)
        cur += 1
    
    ans = 0
    for i in first:
        if i in sec:
            ans += 1
    # print(first)
    # print(sec)
    print(ans)

          
            
               
     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()