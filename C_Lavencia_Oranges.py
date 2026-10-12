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


maxx = 200000
l = [0]
maxval = 0
while l[-1] < maxx:
    
    maxval += 1
    cur = 0
    
    for s in range(1, maxval+1):
        cur += s * (maxval // s)
    l.append(cur)

          
def solve():
    n = getInt()
    
    left, right = 1, len(l) - 1
    
    
    
    while left < right:
        
        mid = (left + right) // 2
        
        if l[mid] >= n:
            right = mid
        else:
            left = mid + 1



    
    c = [0] * (left + 1)
    rem = n
    sizes = []
    while rem > 0:
        
        for s in range(min(left, rem), 0, -1):
            
            if c[s] < left // s:
                c[s] += 1
                sizes.append(s)
                rem -= s
                break
    
    print(left)
    ans = []
    val = 1
    for value in sizes:
        ans.extend([val] * value)
        val += 1
    print(*ans)
    
        
      
             
    
for _ in range(t):
    solve()