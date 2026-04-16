
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
    l = getIntList()

    i = 0

    while i < n:

        count = 0

        val = l[i]
        while i < n and val == l[i]:
            count += 1
            i += 1
        if count >= m:
            print("NO")
            return
    print("YES")



    

                                  
    


          
            
               
     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()