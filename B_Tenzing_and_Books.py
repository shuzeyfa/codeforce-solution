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
    n, x = getIntList()
    a = getIntList()
    b = getIntList()
    c = getIntList()
    
    ans = 0
    
    for i in a:
        if i | x <= x:
            ans = ans | i
        else:
            break
    
    for i in b:
        if i | x <= x:
            ans = ans | i
        else:
            break
    
    for i in c:
        if i | x <= x:
            ans = ans | i
        else:
            break
    
    if ans == x:
        print("Yes")
    else:
        print("No")
        
    
             
    
for _ in range(t):
    solve()