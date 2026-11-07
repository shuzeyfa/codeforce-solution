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
    left, right = getIntList()
    
    l = [i for i in range(left, right+1)]
    
    ans = 0
    summ = 0
    
    for i in range(left, right+1):
        summ += i
        
    count = 0
    
    if 0 in l:
        count += 1
    for i in range(1, max(l)+1):
        if i in l and -i in l:
            count += 2
        else:
            break
        
        
    
    
    if summ in l:
        print(0)
    else:
        n = right - left + 1
        print(n - 1 - count)
        
        
    
             
    
for _ in range(t):
    solve()