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
    l = getIntList()
    
    if m == 1:
        print(max(l))
        return
    
    heap = []
    summ = 0
    for i in range(m-1):
        heapq.heappush(heap, -l[i])
        summ += l[i]
    
    ans = float('-inf')
    minn = 0
    # print(heap)
    for i in range(m-1, n):
        ans = max(ans, m*l[i] - summ)
        val = -heapq.heappop(heap)
        if val <= l[i]:
            heapq.heappush(heap, -val)
        else:
            summ -= val
            summ += l[i]
            heapq.heappush(heap, -l[i])
        # print(heap)
        
    
    print(ans)
        
    
             
    
for _ in range(t):
    solve()