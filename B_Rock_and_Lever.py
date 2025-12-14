
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

    count = defaultdict(int)

    for i in range(n):

        count[l[i].bit_length()] += 1

    ans = 0

    for i in count:
        val = count[i]

        ans += ((val*(val-1)) // 2)
    print(ans)

    


                                  
    


          
            
               
     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()