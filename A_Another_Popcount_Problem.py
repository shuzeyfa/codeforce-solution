
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
    n, k = getIntList()
    
    ans = 0
    
    cur = 0
    
    while True:
        
        summ = k * (2 ** cur)
        cur += 1
        
        if summ <= n:
            ans += k
            n -= summ
        else:
            val = 2 ** (cur - 1)
            ans += n // val
            break
    
    print(ans)
              
               
     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()