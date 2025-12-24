
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
# t = getInt()

   
          
def solve():
    n = getInt()

    a = getIntList()
    b = getIntList()

    a.reverse()
    b.reverse()

    d = defaultdict(int)

    for i in range(n):
        d[a[i]] = i

    final = -1

    ans = 0

    for i in b:
        ind = d[i]

        if ind > final:
            final = ind
        else:
            ans += 1
            # final = ind
    print(ans)



          
            
               
     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()