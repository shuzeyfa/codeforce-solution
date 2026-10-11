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
    l = getIntList()
    
    d  = defaultdict(int)
    val = [0]*n
    
    for i in range(4, n):
        val[i] = l[i-4] + l[i-2] - l[i]
        d[val[i]] += 1
    
    
    
    ans = 0
    for count in d.values():
        ans += count * (count - 1) // 2
        
        
    for i in range(4, n):
        if i - 2 >= 4 and val[i] == val[i-2]:
            ans -= 1
        if i - 4 >= 4 and val[i] == val[i-4]:
            ans -= 1



    print(ans)
        
        
    
    
    
      
             
    
for _ in range(t):
    solve()