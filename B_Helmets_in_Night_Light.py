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
    a = getIntList()
    b = getIntList()
    
    val = []
    
    for i in range(n):
        val.append((b[i], a[i]))
    
    val.sort(key=lambda x:(x[0], -x[0]))
    
    ans = k
    rem = n - 1
    
    for cost, people in val:
        
        if rem == 0:
            break
        
        
        if cost >= k:
            ans += (rem *k)
            break
            
            
            
        used = min(rem, people)
        
        ans += (used * cost)
        rem -= used
    print(ans)
        
        
            
        
    
             
    
for _ in range(t):
    solve()