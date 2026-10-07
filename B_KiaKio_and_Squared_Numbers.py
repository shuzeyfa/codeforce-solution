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
    
    cycle =[4, 16, 37, 58, 89, 145, 42, 20]
    
    position = {}
    for i in range(8):
        position[cycle[i]] = i
    
    d = defaultdict(int)
    res = 0


    for i in range(n):

        val = l[i]
        steps = 0

        while True:

            if val == 1:
                key = "happy"
                break

            if val in position:
                key = (position[val] - steps) % 8
                break

            total = 0

            while val:
                digit = val % 10
                total += digit * digit
                val //= 10

            val = total
            steps += 1

        res += d[key]
        d[key] += 1

    print(res)
        


for _ in range(t):
    solve()