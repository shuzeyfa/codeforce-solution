import sys, os
import math, heapq
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


t = getInt()


def solve():
    n, k = getIntSeq()

    l = []
    for _ in range(n):
        l.append(getIntList())

    # [sum, can_increase]
    d = []

    for a, b, c in l:
        val = a + b + c

        if a == b == c:
            d.append([val, 0])
        else:
            d.append([val, 1])

    d.sort()

    # If the smallest laboratory is stuck,
    # nothing can make the answer larger than it.
    if d[0][1] == 0:
        print(d[0][0])
        return

    # We only need to work with active laboratories.
    # Raise the smallest values toward the next value.
    i = 0

    while i < n - 1:
        # If this laboratory is stuck, it becomes the final upper bound.
        if d[i][1] == 0:
            print(d[i][0])
            return

        # Number of active labs currently at this level.
        j = i + 1
        while j < n and d[j][0] == d[i][0] and d[j][1] == 1:
            j += 1

        # Find next different value.
        if j == n:
            break

        diff = d[j][0] - d[i][0]
        cnt = j - i

        need = diff * cnt

        if k < need:
            print(d[i][0] + k // cnt)
            return

        k -= need
        i = j

    # All active laboratories are now at the same level,
    # so distribute the remaining operations equally.
    cnt = n - i

    # If there are stuck laboratories after i, they cap the answer.
    for j in range(i, n):
        if d[j][1] == 0:
            print(min(d[j][0], d[i][0] + k // cnt))
            return

    print(d[i][0] + k // cnt)


for _ in range(t):
    solve()