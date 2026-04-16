
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

    s += s

    maxx = 0

    for i in range(n):

        count = 0
        ind = i

        while ind < i+n:
            val = s[ind]

            while ind < i+n and  val == s[ind]:
                ind += 1
            count += 1
        maxx = max(maxx, count)
    print(maxx)    
                                  
    


          
            
               
     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()