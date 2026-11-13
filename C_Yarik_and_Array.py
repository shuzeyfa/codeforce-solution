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
    
    ans = float("-inf")
    
    ind = 0
    summ = 0
    parity = None

    
    while ind < n:
        
        if parity == None:
            summ += l[ind]
            parity = 1 - (l[ind]%2)
        elif parity == l[ind]%2:
            summ += l[ind]
            parity = 1 - parity
        else:
            summ = l[ind]
            parity = 1 - (l[ind]%2)
        
        ans = max(ans, summ)
        ind += 1
        if summ < 0:
            summ = 0
            
    print(ans)
        
    
             
    
for _ in range(t):
    solve()