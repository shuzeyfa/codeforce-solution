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
    n, m = getIntList()
    a = getIntList()
    b = getIntList()
    
    if n < 2 * m:
        print("NO")
        return
    
    a.sort()
    b.sort()
    
    ind = 0
    for i in range(m):
        while ind < n and a[ind] < b[i]:
            ind += 1
        if ind < i + 1:
            print("NO")
            return
    
    ind = n - 1
    for i in range(m - 1, -1, -1):
        needed = m - i
        while ind >= 0 and a[ind] > b[i]:
            ind -= 1
        if (n - 1 - ind) < needed:
            print("NO")
            return
    
    print("YES")


for _ in range(t):
    solve()