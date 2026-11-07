import sys, os
import math, heapq
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
    
    val = 1 << n.bit_length()
    
    ans = 0
    for i in range(1, n+1):
        ans ^= i
    
    change= []
    while val > 1:
        
        if val & ans == 0:
            change.append(val // 2)
            ans ^= val
            ans ^= (val // 2)
        val //= 2
    
    l = [0]*n
    
    for i in change:
        l[i-1] = 1
    
    print(*l)             
      
    
    
        
    
             
    
for _ in range(t):
    solve()