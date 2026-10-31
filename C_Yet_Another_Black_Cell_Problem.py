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
    n, x = getIntList()
    l = getIntList()
    l.sort()
    
    
    def check(dist):
        bad = [False] * n

       
        for i in range(n):
            left_is_bad = True
            right_is_bad = True

            if i > 0:
                if l[i] - l[i - 1] <= dist:
                    left_is_bad = False

            if i < n - 1:
                if l[i + 1] - l[i] <= dist:
                    right_is_bad = False

            if left_is_bad and right_is_bad:
                bad[i] = True

       
        need = 0
        i = 0

        while i < n:
            if bad[i] == False:
                i += 1
                continue

            if i + 1 < n:
                if bad[i + 1] == True:

                    gap = l[i + 1] - l[i]

                    if gap <= 2 * dist:
                        need += 1
                        i += 2
                        continue

            need += 1
            i += 1

        return need <= x

    
    left, right = 1, 10 ** 9
    ans = right
    
    while left <= right:
        
        mid = (left + right) // 2
        if check(mid):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    print(ans)
    
             
    
for _ in range(t):
    solve()

