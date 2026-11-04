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
    n, char = getStrList()
    n = int(n)
    s = getStr()
    s += s
    
    if char == 'g':
        print(0)
        return
    
    green = []
    for i in range(n+n):
        if s[i] == 'g':
            green.append(i)
    
    ans = 0
    # print(green)
    for i in range(n):
        if s[i] == char:
            ind = bisect_left(green, i)
            # print(ind, i, green[ind])
            ans = max(ans, green[ind] - i)
    print(ans)
    
        
    
             
    
for _ in range(t):
    solve()