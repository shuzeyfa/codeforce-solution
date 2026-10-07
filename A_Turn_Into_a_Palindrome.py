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
    acc = getStrList()
    n, char = int(acc[0]), acc[1]
    s = getStr()
    
    ind = 0
    ans = 0
    last = n - 1
    while ind < n // 2:
        if s[ind] != s[last]:
            if s[ind] == char or s[last] == char:
                ans += 1
            else:
                ans += 2
        ind += 1
        last -= 1
            
    print(ans)
        


for _ in range(t):
    solve()