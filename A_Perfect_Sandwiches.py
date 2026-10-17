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
    cheese, sau = getIntList()
    
    if sau >= cheese:
        print(-1)
        return
    
    if cheese >= 2*sau:
        print(sau)
        return
    
    ans = 1
    
    while cheese > sau:
        cheese -= 2
        sau -= 1
        if cheese > sau:
            ans += 1
        else:
            break
    print(ans)
    
        
      
             
    
for _ in range(t):
    solve()