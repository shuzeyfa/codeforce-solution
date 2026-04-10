
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
    s= list(getStr())

    count = 0

    if s[0] != "s":
        count += 1
    
    if s[-1] != "s":
        count += 1
    
    s[0] = s[-1] = "s"

    for i in range(1, len(s)-1):
        if s[i] == "u" and (s[i-1] != "s" or s[i+1] != "s"):
            count += 1
            s[i-1] = "s"
            s[i+1] = "s"
    print(count)
                                  
    


          
            
               
     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()