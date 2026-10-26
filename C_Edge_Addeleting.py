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
    n, m = getIntList()
    d = defaultdict(list)
    
    for i in range(n-1):
        u, v = getIntList()
        d[u-1].append(v-1)
        d[v-1].append(u-1)
    
    v = getIntList()
    check = [False]*n
    
    for i in v:
        check[i-1] = True
    
    
    q = deque()
    q.append([n-1, 0])
    # print(q)
    ans = 0
    visited = [False]*n
    visited[n-1] = True
    visited[0] = True
    
    
    # print(d)
    while q:
        ind, val = q.popleft()
        # print(ind+1, val)
        if check[ind]:
            ans = max(ans, val + 1)
            
        
        for i in d[ind]:
            if i == 0:
                ans = max(ans, val+1)
                continue
            if not visited[i]:
                visited[i] = True
                q.append([i, val + 1])
                # print(i+1, val+1, ind+1)
            
    print(ans)
            
            
        
        
    
             
    
for _ in range(t):
    solve()