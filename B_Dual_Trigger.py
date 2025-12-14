
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
    s = getStr()

    if n == 1:
        if s[0] == "0":
            print("YES")
            return
        print("NO")
        return
    
    if n == 2 and s[0] == s[1] == "0":
        print("YES")
        return
    if n == 2:
        print("NO")
        return
    
    ind = []
    for i in range(n):
        if s[i] == "1":
            ind.append(i)
    if len(ind) == 2 and ind[1] - ind[0] == 1:
        print("NO")
        return
    
    if len(ind)%2 == 0:
        print("YES")
    else:
        print("NO")
    
                                  
    


          
            
               
     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()