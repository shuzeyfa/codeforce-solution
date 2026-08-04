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
    n, k = getIntList()
    s = getStr()

    l = list(s)

    if 2 * k > n:
        print(-1)
        return

    ans = 0

    for i in range(k):
        if l[i] != "R":
            ans += 1

    for i in range(n - k, n):
        if l[i] != "L":
            ans += 1

    print(ans)


for _ in range(t):
    solve()