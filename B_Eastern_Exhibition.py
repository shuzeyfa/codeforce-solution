
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

    x = []
    y = []
    for i in range(n):
        x1, y1 = getIntList()
        x.append(x1)
        y.append(y1)
    
    if n%2 == 1:
        print(1)
        return
    
    x.sort()
    y.sort()

    # print(x)
    # print(y)
    val_x = x[n//2] - x[n//2 - 1] + 1
    val_y = y[n//2] - y[n//2 - 1] + 1

    print(val_x * val_y)

    
    
    
                                  
    


          
            
               
     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()