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
    s = getStr()
    
    ind = -1
    
    for i in range(1, n-1):
        if s[i] != s[i-1] and s[i+1] != s[i] and s[i-1] == s[i+1]:
            ind = i
            break
    
    # print(ind)
    if ind == -1:
        for i in range(1, n-1):
            if s[i] != s[i-1] and s[i+1] != s[i]:
                ind = i
                break
    if ind != -1:
        val = s[:ind] + s[ind+1:]
    else:
        val = s
    
    count = 0
    # print(val)
    ind = 0
    while ind < len(val):
        cur = val[ind]
        
        while ind < len(val) and val[ind] == cur:
            ind += 1
        count += 1
    print(count)
        


for _ in range(t):
    solve()