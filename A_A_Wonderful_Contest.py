
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

    ans = []

    for i in range(n):
        ans.append(100 // l[i])
    
    ans.sort(reverse=True)
    
    for i in range(100*n + 1):
        
        val = i
        
        for j in ans:
            val %= j
        
        if val != 0:
            print("No")
            return
    
    print("Yes") 

          
            
               
     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()