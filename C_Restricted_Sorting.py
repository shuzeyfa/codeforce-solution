
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
    l= getIntList()

    dif = []

    val = l[:]
    val.sort()

    for i in range(n):
        if val[i] != l[i]:
            dif.append(l[i])

    if len(dif) == 0:
        print(-1)
        return

    dif.sort()

    minn = float("inf")

    for i in range(len(dif)):
        
        minn = min(abs(dif[i] - dif[-1]), minn)
        minn = min(minn, abs(dif[i] - dif[0]))
    print(minn)     
                                  
    


          
            
               
     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()