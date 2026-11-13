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
    s = getStr()
    
    maxx = float('-inf')
    minn = float('inf')
    
    
    
    # par = [i for i in range(26)]
    
    
    left, right = 0, n - 1
    ans = 0
    
    val = []
    
    while left < right:
       
        first = ord(s[left]) - ord("a")
        sec = ord(s[right]) - ord("a")
        
        if first != sec:
            val.append((min(first, sec), max(first, sec)))
        left += 1
        right -= 1
        
        
    val.sort()

    merged = []
    

    for l, r in val:
        if not merged or l > merged[-1][1]:
            merged.append([l, r])
        else:
            merged[-1][1] = max(merged[-1][1], r)
    # print(merged)
    for left, right in merged:
        ans += (right - left)
    print(ans)
        
    
             
    
for _ in range(t):
    solve()