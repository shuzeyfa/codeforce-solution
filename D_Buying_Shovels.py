
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
    n, k =getIntList()

    div = 2

    ans = [1]
    another = []
                                  
    while div*div <= n:
        if n%div == 0:
            ans.append(div)
            if div != n // div:
                another.append(n // div)
        div += 1
    for i in another[::-1]:
        ans.append(i)
    ans.append(n)
    

    left, right = 0, len(ans) - 1
    ind = left

    while left <= right:
        mid = (left + right) // 2

        if ans[mid] <= k:
            ind = mid
            left = mid + 1
        else:
            right = mid - 1
    print(n // ans[ind])

          
            
               
     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()