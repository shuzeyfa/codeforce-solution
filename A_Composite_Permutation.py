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
    if n <= 3:
        print(-1)
        return
    
    if n%2 == 0:
        print(*[i for i in range(n, 0, -1)])
    else:
        ans = [i for i in range(n-1, 0, -1)]
        ans.append(n)
        print(*ans)
        
    
             
    
for _ in range(t):
    solve()