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
    
    e1 = e2 = o1 = o2 = 0
    
    for i in a:
        if i%2 == 0:
            e1 += 1
        else:
            o1 += 1
    
    for i in b:
        if i%2 == 0:
            e2 += 1
        else:
            o2 += 1
    
    if e1 != e2 and e1 > e2 and k%2 == 0:
        print("NO")
        return
    
    if e1 != e2 and e2 > e1 and k%2 == 1:
        print("NO")
        return
    
    print("YES")
        
    
             
    
for _ in range(t):
    solve()