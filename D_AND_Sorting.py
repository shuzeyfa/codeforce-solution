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
    
    dif = []
    
    for i in range(n):
        if i != l[i]:
            dif.append(l[i])
    
    val = dif[0]
    
    for i in range(1, len(dif)):
        val &= dif[i]
    
    for i in range(n-1, -1, -1):
        if val & i >= val:
            print(val)
            return
        
    
             
    
for _ in range(t):
    solve()