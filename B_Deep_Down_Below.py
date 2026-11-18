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
    l = []
    
    for i in range(n):
        val = getIntList()
        maxx = float('-inf')
        
        for j in range(val[0]):
            temp = val[j+1] - j
            maxx = max(maxx, temp)
        l.append((maxx, val[0]))
    
    l.sort()
    # print(l)
    ans = l[0][0] + 1
    power = l[0][0] + l[0][1] + 1
    # print(ans, power)
    
    for i in range(1, n):
        if power <= l[i][0]:
            rem = l[i][0] + 1 - power 
            power += rem
            ans += rem
        power += l[i][1]
        
    print(ans)
         
    
        
      
             
    
for _ in range(t):
    solve()