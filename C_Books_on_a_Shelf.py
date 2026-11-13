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
    l = getIntList()
    
    d = Counter(l)
    
    s = list(set(l))
    s.sort()
    
    rem = []
    
    for i in d:
        rem += [i]*(d[i]-1)
    rem.sort(reverse=True)
    
    ans = s[:] + rem
    
    print(len(set(rem)) + len(s))
    print(*ans)
    # print()
    
    
        
    
             
    
for _ in range(t):
    solve()