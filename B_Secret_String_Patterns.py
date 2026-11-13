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
    
    print("?", 1, n)
    sys.stdout.flush()
    val = getInt()
    
    
    
    if val == 0 or val == n:
        print("! NO")
        sys.stdout.flush()
        return
    
    print("?", 1, val)
    sys.stdout.flush()
    left = getInt()
    
    print("?", val+1, n)
    sys.stdout.flush()
    right = getInt()
    
    if left == val and right == 0:
        print("! NO")
        
    else:
        print("! YES")
    sys.stdout.flush()
    
        
    
             
    
for _ in range(t):
    solve()