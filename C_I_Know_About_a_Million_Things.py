
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
    n = getInt()
    l = getIntList()

    odd = 0
    even = 0

    for i in l:
        if i % 2 == 1:
            odd += 1
        else:
            even += 1

    if even == 1 and odd == 1:
        print("Larpity")
    elif even == 0 and odd == 3:
        print("Larpity")
    else:
        print("Moggity")


for _ in range(t):
    solve()
