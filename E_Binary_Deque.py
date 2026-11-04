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
    
    if sum(l) < k:
        print(-1)
        return
    
    if sum(l) == k:
        print(0)
        return
    
    rem = sum(l) - k
    pre = []
    suf = []
    
    for i in range(n):
        if l[i] == 1:
            pre.append(i+1)
    
    ind = 1
    for i in range(n-1, -1, -1):
        if l[i] == 1:
            suf.append(ind)
        ind += 1
    # print(pre)
    
    ans = float('inf')
    
    for i in range(rem+1):
        x = rem - i
        y = i
        
        val = 0
        if x > 0:
            val += pre[x-1]
        if y > 0:
            val += suf[y-1]
        ans = min(ans, val)
    print(ans)
        
        
        
    
             
    
for _ in range(t):
    solve()