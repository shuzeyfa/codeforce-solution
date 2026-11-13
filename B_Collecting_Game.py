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
    d = defaultdict(list)
    for i in range(n):
        d[l[i]].append(i)
        
    l.sort()
    
    pre = [l[0]]
    
    for i in range(1, n):
        pre.append(pre[-1] + l[i])
    
    val = []
    
    for i in range(n-1, -1, -1):
        ind = bisect_right(l, pre[i])
        val.append(ind - 1)
    
    val.reverse()
    # print(val)
    res = [0]*n
    res[-1] = val[-1]
    for i in range(n-2, -1, -1):
        res[i] = max( res[val[i]], val[i])

    
    ans = [0]*n
    
    for i in range(n):
        place = d[l[i]].pop()
        ans[place] = res[i]
    print(*ans)
        
    
        
    
             
    
for _ in range(t):
    solve()