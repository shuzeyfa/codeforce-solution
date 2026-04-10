
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

sys.setrecursionlimit(10**5 + 200)

t = 1
t = getInt()

   
          
def solve():
    n = getInt()
    l = getIntList()

    dp = [0] * (n+1)

    for i in range(n - 1, -1, -1):
        include = float('inf')
        if i + l[i] < n:
            include = dp[i + l[i] + 1]
        
        exclude = dp[i + 1] + 1
        
        dp[i] = min(include, exclude)
    
    print(dp[0])


     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()