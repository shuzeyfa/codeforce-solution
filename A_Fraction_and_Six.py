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
    a = getStr()
    b = getStr()
    
    l1 = list(a)
    l2 = list(b)
    
    if 's' not in a or 'i' not in a or 'x' not in a:
        print("NO")
        return
    l1.remove('s')
    l1.remove('i')
    l1.remove('x')
    
    if sorted(l1) != sorted(l2):
        print("NO")
    else:
        print("YES")
     
    
             
    
for _ in range(t):
    solve()