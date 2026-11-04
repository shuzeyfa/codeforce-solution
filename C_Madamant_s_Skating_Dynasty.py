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


t = 1
t = getInt()


mod = 998244353

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0

    g, x1, y1 = extended_gcd(b, a % b)

    x = y1
    y = x1 - (a // b) * y1

    return g, x, y


def mod_inverse(a, m):
    g, x, y = extended_gcd(a, m)

    if g != 1:
        return None

    return x % m
      
def solve():
    n = getInt()
    l = getIntList()
    
    
    l.sort()
    
    pre = [l[0]]
    for i in range(1, n):
        pre.append(pre[-1] + l[i])
        
    factorial = 1
    
    for i in range(2, n):
        factorial = (factorial * i) % mod
    
    ans = 0
    for i in range(n-1):
        rem = n - i - 1
        val = val = factorial * mod_inverse(rem, mod) % mod
        
        res = (val * ((pre[-1] - pre[i] - ((l[i]*rem) % mod)) % mod)) % mod
        ans = (ans + res) % mod
        
    print(ans)
        
    
             
    
for _ in range(t):
    solve()