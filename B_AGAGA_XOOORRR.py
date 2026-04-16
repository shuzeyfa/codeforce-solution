
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

    total = 0

    for i in range(n):
        total ^= l[i]
    
    if total == 0:
        print("YES")
        return

    count = 0

    cur = 0

    for i in l:
        cur ^= i

        if cur == total:
            cur = 0
            count += 1
    
    if count >= 3:
        print("YES")
    else:
        print("NO")
                                  
    



            
               
     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()