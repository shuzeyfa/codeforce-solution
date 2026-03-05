
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

    ans = 1
    val1 =  val2 = 0

    

    for i in s:
        if i == ">":
            val1 += 1
            val2 = 0
        else:
            val1 = 0
            val2 += 1
        ans = max(val1, val2)
    print(ans+1)


          
            
               
     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()