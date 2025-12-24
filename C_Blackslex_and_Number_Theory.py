
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
    # print(l)
    

    left, right = min(l) + 1, 10**9
    ans = min(l)

    def check(num):
        for i in range(1, n):
            rem = l[i] - num
            if rem < l[0]:
                return False
        return True
    # print(check(6))

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