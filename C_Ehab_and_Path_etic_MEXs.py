
import sys, os
import math
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
# t = getInt()

   
          
def solve():
    n = getInt()

    edges = []
    deg = [0] * (n + 1)

    for _ in range(n - 1):
        u, v = map(int, input().split())
        edges.append((u, v))
        deg[u] += 1
        deg[v] += 1

    special = -1
    for i in range(1, n + 1):
        if deg[i] >= 3:
            special = i
            break

    ans = [-1] * (n - 1)

    if special != -1:
        cur = 0
        for i in range(n - 1):
            u, v = edges[i]
            if u == special or v == special:
                if cur < 3:
                    ans[i] = cur
                    cur += 1

    cur = 0 if special == -1 else 3
    for i in range(n - 1):
        if ans[i] == -1:
            ans[i] = cur
            cur += 1

    for i in ans:
        print(i)
                                  
    


          
            
               
     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()