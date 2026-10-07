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
    
    count = Counter(l)
    uniques = sorted(count.keys())
    
    if not uniques or uniques[0] != 0:
        print(-1)
        return
    
    current = 0
    prev = 0
    val = defaultdict(int)
    
    for i in range(len(uniques)):
        if uniques[i] != current:
            print(-1)
            return
        
        m = count[uniques[i]]
        
        if i == len(uniques) - 1:
            value = prev + 1
        else:
            next_s = uniques[i + 1]
            diff = next_s - current
            if diff % m != 0:
                print(-1)
                return
            value = diff // m
            if value <= prev:
                print(-1)
                return
        
        val[uniques[i]] = value
        current += m * value
        prev = value
    
    a = [val[x] for x in l]
    print(*a)


for _ in range(t):
    solve()