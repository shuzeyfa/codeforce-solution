
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
    s = getStr()   
    n = len(s)  

    l = list(s)

    for i in range(1, n):
        if l[i] != l[i-1]:
            continue

        for j in "abcdefghijklmnopqrstuvwxyz":
            if j != l[i-1] and (i+1 == n or l[i+1] != j):
                l[i] = j
                break
    print("".join(l))


                                  
    


          
            
               
     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()