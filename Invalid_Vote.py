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
    n, m = getIntList()
    
    l = []
    
    for i in range(n):
        s = getStr()
        l.append(s)
    
    d = defaultdict(int)
    for j in range(m):
        s = getStr()
        if s in l:
            d[s] += 1
        else:
            sec = defaultdict(int)
            for i in range(len(s)):
                for j in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
                    val = s[:i] + j + s[i+1:]
                    if val in l:
                        sec[val] += 1
            count = 0
            for i in l:
                if sec[i] > 0:
                    count += 1
            if count > 1:
                continue
            else:
                for i in l:
                    if sec[i] > 0:
                        d[i] += 1
    
    for i in l:
        print(d[i])
    
    
        
      
             
    
for _ in range(t):
    solve()