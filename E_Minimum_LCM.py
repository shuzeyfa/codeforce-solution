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
    
    def find(num):
        
        for i in range(2, int(math.sqrt(num))+1):
            if num%i == 0:
                return i
        return num
    
    val = find(n)
    if val == n:
        print(1, n-1)
    else:
        ans = n // val
        print(ans, n - ans)
        
    
             
    
for _ in range(t):
    solve()