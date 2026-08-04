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
    n, k, m = getIntSeq()

    if k > m:
        print("NO")
        return

    print("YES")

    res = []
    for i in range(1, n + 1):
        if i % k == 0:
            res.append(m - k + 1)
        else:
            res.append(1)

    print(*res)


for _ in range(t):
    solve()