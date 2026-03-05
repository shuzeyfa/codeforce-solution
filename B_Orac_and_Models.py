
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


    dp = [1]*n

    for i in range(n):

        j = 2 * (i + 1)

        while j <= n:
            if l[i] < l[j-1]:
                dp[j-1] = max(dp[j-1], dp[i] + 1)
            j += i + 1
    print(max(dp))



          
            
               
     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()