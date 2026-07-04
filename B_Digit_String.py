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
    s = getStr()
    
    ans = 0
    l = []
    
    for i in s:
        if i == "4":
            ans += 1
        else:
            l.append(i)
    
    if len(l) == 0:
        print(ans)
        return
    if len(l) == 1 and l[0] == "2":
        print(ans)
        return
    
    m = len(l)
    prefix = [0] * (m + 1)
    for i in range(m):
        prefix[i + 1] = prefix[i] + (1 if l[i] == "2" else 0)
    
    total_non2 = m - prefix[m]
    maxx = 0
    
    for k in range(m + 1):
        keep = total_non2 - (k - prefix[k])
        kept = prefix[k] + keep
        if kept > maxx:
            maxx = kept
    
    print(ans + m - maxx)
    
    
for _ in range(t):
    solve()