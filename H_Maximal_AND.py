
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
    n, k =getIntList()
    l = getIntList()

    ans = 0

    for i in range(30, -1, -1):
        rem = 0

        val =  (1 << i)  
        for j in l:
            if val & j == 0:
                rem += 1
        if rem <= k:
            ans += val
            k -= rem

    print(ans)

          
            
               
     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()