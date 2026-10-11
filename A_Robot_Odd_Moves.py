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
    x, y  = getIntList()
    
    if y - 1 > x:
        print(-1)
        return
    if y -1 ==x:
        print(y)
        return
    
    rem = x%2 == y%2
    
    if rem:
        print(x)
    else:
        print(x+1)
    
        
      
             
    
for _ in range(t):
    solve()