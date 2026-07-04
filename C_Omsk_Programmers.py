
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
    a, b, x = getIntList()
     
    ans = max(a, b) - min(a, b)
    cur = 0
    
    maxx, minn = max(a, b), min(a, b)
    
    while maxx != minn:
        
        cur += 1
        maxx //= x
        
        if maxx < minn:
            val = maxx
            maxx = minn
            minn = val
        
        cost = cur + (maxx - minn)
        ans = min(cost, ans)
    print(ans)
        
        
                     
    
                      
    
for _ in range(t):
    solve()