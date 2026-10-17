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
    n, k  = getIntList()
    
    l = getIntList()
    
    ind = defaultdict(list)
    
    ind[0].append(0)
    
    summ = 0
    ans = 0
    
    for i in range(n):
        summ += l[i]
        rem = summ % k
        
        
        val = bisect_left(ind[rem], i + 1 - k)
        ans += val
        ind[rem].append(i+1)
    print(ans)
    
    
        
      
             
    
for _ in range(t):
    solve()