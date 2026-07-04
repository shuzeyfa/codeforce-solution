
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
t = getInt()

   
          
def solve():
    n = getInt()
    l = getIntList()
    
    s = list(set(l))
    s.sort()
    
    if len(s) == 1 and l[0] == 0:
        print(n)
        return
    
    maxx = max(l)
    
    ans = n * maxx
    
    mex = 0
    
    for i in range(len(s)-1):
        
        while mex == s[i] or mex == maxx:
            mex += 1
        
        ans += mex
    
    ans += (mex * (n - len(s)))
    print(ans)
    # print(s)
    
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()