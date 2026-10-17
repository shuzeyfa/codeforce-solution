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
# t = getInt()


          
def solve():
    n, k, final = getIntList()
    l = getIntList()
    l.sort()
    
    temp = [a for a in l if a <= final]
    if not temp:
        print((final + k - 1) // k)
        return
    
    ans = math.ceil(l[0] / k)
    
    cur  = max(ans * k, l[0] + k)
    
    for i in range(1, n):
        if cur >= final:
            break
        
        if cur >= l[i]:
            cur = max(l[i] + k, cur)
            continue
        
        rem = min(l[i], final) - cur
        cost = math.ceil(rem / k)
        ans += cost
        
        cur += cost*k
        cur = max(cur, l[i] + k)
    # print(ans)
    if cur < final:
        rem = final - cur
        ans += math.ceil(rem / k)
    print(ans)
    
        
      
             
    
for _ in range(t):
    solve()