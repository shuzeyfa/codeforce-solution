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


def calc(l, n):
    d = [abs(l[i] - l[i + 1]) for i in range(n - 1)]
    ans = max(d)
    p = d.index(ans)                 # first max edge
    pre = max(d[:p], default=0)      # edges before p

    suf = d + [0, 0]                 # suf[i] = max(d[i:])
    for i in range(n - 2, -1, -1):
        suf[i] = max(suf[i], suf[i + 1])

    mid = 0
    for r in range(p + 1, n):        # segment is [p+1, r]
        if r > p + 1:
            inner = max(mid, 2 * d[r - 1])
        cur = max(pre, mid, abs(l[p] - 2 * l[r]), suf[r + 1])
        if r < n - 1:
            cur = max(cur, abs(2 * l[p + 1] - l[r + 1]))
        ans = min(ans, cur)

    return ans


def solve():
    n = getInt()
    l = getIntList()
    
    dif = []
    
    for i in range(n-1):
        dif.append(abs(l[i] - l[i+1]))
    
    ans = max(dif)
    
    ind = dif.index(ans)
    
    if ind > 0:
        left = max(dif[:ind])
    else:
        left = 0
        
    right = dif + [0, 0]
    
    

    for i in range(n - 2, -1, -1):
        right[i] = max(right[i], right[i + 1])
        
        

    mid = 0
    for r in range(ind + 1, n):        
        if r > ind + 1:
            mid = max(mid, 2*dif[r-1])
            
            
        cur = max(left, mid, abs(l[ind] - 2*l[r]), right[r + 1])
        if r < n - 1:
            cur = max(cur, abs(2 * l[ind+1] - l[r+1]))
        ans = min(ans, cur)

    res1 = ans
    
    l.reverse()
    dif = []
        
    for i in range(n-1):
        dif.append(abs(l[i] - l[i+1]))
    
    ans = max(dif)
    
    ind = dif.index(ans)
    
    if ind > 0:
        left = max(dif[:ind])
    else:
        left = 0
        
    right = dif + [0, 0]
    
    

    for i in range(n - 2, -1, -1):
        right[i] = max(right[i], right[i + 1])
        
        
    mid = 0
    for r in range(ind + 1, n):        
        if r > ind + 1:
            mid = max(mid, 2*dif[r-1])
            
            
        cur = max(left, mid, abs(l[ind] - 2*l[r]), right[r + 1])
        if r < n - 1:
            cur = max(cur, abs(2 * l[ind+1] - l[r+1]))
        ans = min(ans, cur)
    res2 = ans
    
    print(min(res1, res2))

for _ in range(t):
    solve()