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
    
    left = float('inf')
    
    for _ in range(n):
        temp = getIntList()
        left = min(left, sum(temp))
        if temp[0] > temp[1] or temp[1] > temp[2]:
            l.append((sum(temp), 0))
        elif temp[0] == temp[1] == temp[2]:
            l.append((sum(temp), -1))
        else:
            l.append((sum(temp), min(temp[1] - temp[0] + 1, temp[2] - temp[1] + 1)))
    
    
    def check(num):
        need = 0
        
        for summ, sign in l:
            if summ >= num:
                continue
            
            if sign == -1:
                return False
            
            need += num - summ + 2 * sign
        return need <= k
    
    
    
    right = left + k
    ans = left
    
    while left <= right:
        mid = (left + right) // 2 
        if check(mid):
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
    
    print(ans)
    
    
    
    

    


for _ in range(t):
    solve()