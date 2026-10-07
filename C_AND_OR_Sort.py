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
    s = getStr()
    
    if s[0] == "1":
        print(s.count("0"))
        return
    
    zero = [1 if s[-1] == "0" else 0]
    one = [0]
    
    for i in range(1, n):
        if s[i] == "1":
            one.append(one[-1] + 1)
        else:
            one.append(one[-1])
    
    for i in range(n-2, -1, -1):
        if s[i] == "0":
            zero.append(zero[-1] + 1)
        else:
            zero.append(zero[-1])
    zero.reverse()
    # print(zero)
    # print(one)
    ans = float("inf")
    
    for i in range(n):
        val = one[i] + zero[i] - 1
        ans = min(ans, val)
    print(ans)
    
    
        


for _ in range(t):
    solve()