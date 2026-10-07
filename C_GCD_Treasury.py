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
    n, x = getIntList()
    l = getIntList()
    
    
    if x == 0:
        print(0)
        return
    
    div = []
    
    i = 1
    
    
    while i * i <= x:
        if x % i == 0:
            div.append(i)
            if i != x // i:
                div.append(x // i)
        i += 1
    
    ans = 0
    for d in div:
        if d == 1:
            continue
        
        s = 0
        for val in l:
            if val % d == 0:
                s += val
                
        if s > ans:
            ans = s
            
            
    print(ans)
    
    
    
        


for _ in range(t):
    solve()