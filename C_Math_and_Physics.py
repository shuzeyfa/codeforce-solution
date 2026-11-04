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
    
    if len(set(l)) == 1 and l[0] == 1:
        print(-1)
        return
    
    
    summ = 0
    
    for i in range(1, n-1):
        if l[i] > 1:
            summ += l[i]
    
    if summ > 0:
        print(sum(l) - 1)
    else:
        print(sum(l) - (n-1))
        
    
             
    
for _ in range(t):
    solve()