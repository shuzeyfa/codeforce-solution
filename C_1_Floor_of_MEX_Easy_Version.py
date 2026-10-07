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
    l = getIntList()
    
    ans = []
    
    minn = 0
    maxx = n
    for i in range(n):
        if l[i] == 0:
            minn = i + 1
    
    for i in range(n-1, -1, -1):
        if l[i] == 1:
            maxx = i + 1
    
    ans = [i for i in range(minn, maxx)]
    print(len(ans))
    print(*ans)
            
    
    
        
    
    
        


for _ in range(t):
    solve()