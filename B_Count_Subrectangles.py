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
# t = getInt()


def solve():
    n, m, k = getIntList()
    a = getIntList()
    b = getIntList()
    
    divisors = []
    
    val = 1
    
    while val * val <= k:
        
        if k%val == 0:
            divisors.append(val)
            if val != k // val:
                divisors.append(k // val)
        val += 1
    # print(divisors)
    
    ind = 0
    
    l1 = []
    l2 = []
    
    while ind < n:
        if a[ind] == 1:
            summ = 0
            while ind < n and a[ind] == 1:
                summ += 1
                ind += 1
            l1.append(summ)
        else:
            ind += 1
    
    ind = 0
    while ind < m:
        if b[ind] == 1:
            summ = 0
            while ind < m and b[ind] == 1:
                summ += 1
                ind += 1
            l2.append(summ)
        else:
            ind += 1
    
    ans = 0
    # print(divisors)
    for div in divisors:
        
        val_a = 0
        for i in l1:
            if i >= div and div != 1:
                val_a += (i - div + 1)
            elif i >= div:
                val_a += i
        
        val_b = 0
        div2 = k // div
        for i in l2:
            if i >= div2 and div2 != 1:
                val_b += (i - div2 + 1)
            elif i >= div2:
                val_b += i
        ans += val_a * val_b
        # print(ans)
    print(ans)
        


for _ in range(t):
    solve()