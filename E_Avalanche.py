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
    n, k = getIntList()
    l = getIntList()
    
    prev = [0]*n
    
    
    summ = 0
    for i in range(n-1, -1, -1):
        
        prev[i] = (l[i] + summ)%2
        summ = (summ+prev[i])%2 
        if i+k < n:
            summ = (summ - prev[i + k]) % 2
        
    if sum(prev)%2 == 0:
        print("Bob")
    else:
        print("Alice")
        
        
        
    
             
    
for _ in range(t):
    solve()