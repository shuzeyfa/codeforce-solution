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
    n, k = getIntSeq()
    a = getIntList()
    
    c = []
    ind = 0
    while ind < n:
        j = ind
        while j < n and a[j] == a[ind]:
            j += 1
        c.append(j - ind)
        ind = j
    
    m = len(c)
    c.sort()
    
    l = []
    ind = 0
    while ind < m:
        j = ind
        while j < m and c[j] == c[ind]:
            j += 1
        l.append((c[ind], j - ind))
        ind = j
    
    p = len(l)
    count = m
    
    ans = 0
    summ = 0
    counted = 0
    
    for ind in range(p + 1):
        if ind == 0:
            hi = l[0][0] - 1
        else:
            val, freq = l[ind - 1]
            summ += val * freq
            counted += freq
            hi = l[ind][0] - 1 if ind < p else None
        
        A = n - summ
        acnt = count - counted
        
        if acnt > 0:
            num = k - A
            if num % acnt == 0:
                S = num // acnt
                if hi is None or S >= -hi:
                    ans += 1
    
    print(ans)


for _ in range(t):
    solve()