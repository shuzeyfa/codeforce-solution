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
# t = getInt()


          
def solve():
    a = getStr()
    d = getStr()
    
    if a[0] == "A" and a[1] == "D":
        print("Yes")
    elif a[0] == "A" and d[0] == "D":
        print("Yes")
        
    elif a[1] == "A" and a[0] == "D":
        print("Yes")
    elif a[1] == "A" and d[1] == "D":
        print("Yes")
        
        
    elif  d[0] == "A" and a[0] == "D" or d[0] == "A" and d[1] == "D":
        print("Yes")
    
    elif d[1] == "A" and d[0] == "D" or d[1] == "A" and a[1] == "D":
        print("Yes")
    else:
        print("No")
    
    
        
      
             
    
for _ in range(t):
    solve()