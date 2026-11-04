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
# t = getInt()


          
def solve():
    n = getInt()
    l = getIntList()
    
    k = sum(l) // 3
    if sum(l)%3 != 0:
        print(0)
        return
    
    prefix = 0
    count = 0
    ans = 0
    
    for i in range(n-1):
        
        prefix += l[i]
        if prefix == 2*k:
            ans += count

        if prefix == k:
            count += 1
        
        
    print(ans)
            
        
    
             
    
for _ in range(t):
    solve()