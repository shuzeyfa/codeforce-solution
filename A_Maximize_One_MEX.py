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
    
    prev = 0
    
    visited = [False]*n
    res = []
    
    for o in range(n):
        visited[l[o]] = True
        getted = False
        for m in range(n):
            if not visited[m]:
                res.append(m)
                getted = True
                break
        if not getted:
            res.append(n)
    res.sort(reverse=True)
    prev = res[k-1]
    
    # print(prev)
    # print(res)
    
    
    ans = [-1]*2
    
    for i in range(n):
        for j in range(i+1, n):
            if  i == j:
                continue
            
            val = l[:]
            first, sec = l[i], l[j]
            val[i] = sec
            val[j] = first
            # print(val)
            
            visited = [False]*n
            res = []
            
            for o in range(n):
                visited[val[o]] = True
                getted = False
                for m in range(n):
                    if not visited[m]:
                        res.append(m)
                        getted = True
                        break
                if not getted:
                    res.append(n)
            res.sort(reverse=True)
            # print(res)
            # print()
            maxx = res[k-1]
            if maxx > prev:
                prev = maxx
                ans[0] = i
                ans[1] = j
    if ans[0] == -1:
        print(-1)
    else:
        print(ans[0] + 1, ans[1] + 1)
    
             
    
for _ in range(t):
    solve()