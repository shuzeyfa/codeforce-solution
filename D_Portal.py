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
    n, x, y = getIntList()
    l = getIntList()
    
    
    a = l[:x]
    b = l[x:y]
    c = l[y:]
    # print(c)
    # print(a)
    
    combined = a + c
    if not b:
        print(*combined)
        return
    
    
    ind = b.index(min(b))
    
    new = b[ind:] + b[:ind]
    
    minn = new[0]
    
    i= 0
    
    while i < len(combined):
        
        if combined[i] > minn:
            ans = combined[:i] + new + combined[i:]
            print(*ans)
            return
        i += 1
    ans = combined + new
    print(*ans)
    
        
    
             
    
for _ in range(t):
    solve()