
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
    n, x, y, z = getIntList()
    n2 = n
    
    val = x * z
    if val >= n:
        ans = math.ceil(n / x)
    else:
        ans = z
        n -= (z * x)
        
        ans += math.ceil(n / (x + y*10))
        
    ans2 = math.ceil(n2 / (x+y))
    print(min(ans, ans2))       
               
     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()