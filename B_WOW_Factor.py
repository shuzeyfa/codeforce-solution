
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
# t = getInt()

   
          
def solve():
    s = getStr()
    n = len(s)

    pre = [0]*n
    suf = [0]*n

    count = 0
    for i in range(1, n):
        if s[i] == "v" and s[i-1] == "v":
            count += 1
        pre[i] = count

    count = 0
    for i in range(n-2, -1,  -1):
        if s[i] == "v" and s[i+1] == "v":
            count += 1
        suf[i] = count

    ans = 0
    for i in range(n):
        if s[i] == "o":
            ans += (suf[i]*pre[i])
    print(ans)
                       
    
        
                     
    
                      
    
for _ in range(t):
    solve()