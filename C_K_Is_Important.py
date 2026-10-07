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

class Fenwick:
    def __init__(self, n):
        self.n = n
        self.t = [0] * (n + 1)
    def add(self, i, v):
        while i <= self.n:
            self.t[i] += v
            i += i & -i
    def find_kth(self, k):
        pos = 0
        bit = 1 << self.n.bit_length()
        while bit:
            nxt = pos + bit
            if nxt <= self.n and self.t[nxt] < k:
                k -= self.t[nxt]
                pos = nxt
            bit >>= 1
        return pos + 1

def solve():
    n, k = getIntSeq()
    a = getIntList()
    fen = Fenwick(n)
    for i in range(1, n + 1):
        fen.add(i, 1)
    m = n
    res = 0
    while m >= k:
        left_pos = fen.find_kth(k)
        right_pos = fen.find_kth(m - k + 1)
        if a[left_pos - 1] >= a[right_pos - 1]:
            res += a[left_pos - 1]
            fen.add(left_pos, -1)
        else:
            res += a[right_pos - 1]
            fen.add(right_pos, -1)
        m -= 1
    print(res)

for _ in range(t):
    solve()