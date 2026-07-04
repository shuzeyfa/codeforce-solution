
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
    l.sort()
    
    def check(num):
        used = [False] * n
        
        remained = []

        for need in range(num + 1):

            pos = -1

            # 1) Try exact match (best choice)
            idx = bisect_left(l, need)
            while idx < n and l[idx] == need:
                if not used[idx]:
                    pos = idx
                    break
                idx += 1

            # 3) If nothing works, stop
            if pos == -1:
                remained.append(need)
                continue

            used[pos] = True
        
        for need in remained[::-1]:
            pos = -1
            
            idx = bisect_left(l, 2 * need + 1)
            while idx < n and used[idx]:
                idx += 1
            if idx < n:
                pos = idx


            # 3) If nothing works, stop
            if pos == -1:
                return False

            used[pos] = True

        return True
    
    ans = 0
    
    left, right = 1, n
    
    while left <= right:
        
        mid = (left + right) // 2
        
        if check(mid):
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
    
    print(ans+1)
    
    
    
            
               
     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()