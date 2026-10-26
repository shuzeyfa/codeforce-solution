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


          
def solve():
    n, m, v = getIntList()
    l = getIntList()
    
    pre = [0]
    for i in range(n):
        pre.append(pre[-1] + l[i])
        
    left = [0]
    summ = 0
    
    for i in range(n):
        summ += l[i]
        
        if summ >= v:
            left.append(i + 1)
            summ = 0
    
    if len(left) <= m:
        print(-1)
        return
    
    right = [n]
    summ = 0
    
    for i in range(n-1, -1, -1):
        summ += l[i]
        
        if summ >= v:
            right.append(i)
            summ =0
    
    ans = 0
    
    for i in range(m+1):
        left_ind = left[i]
        right_ind = right[m - i]
        
        if left_ind <= right_ind:
            val = pre[right_ind] - pre[left_ind]
            ans = max(ans, val)
    
    print(ans) 
            
        
    
             
    
for _ in range(t):
    solve()