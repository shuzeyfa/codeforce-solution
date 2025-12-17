
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
    k, x = getIntList()

    val = (k*(k+1)) // 2     

    if x <= val:
        left, right = 1, k
        ans = 1

        while left <= right:
            mid = (left + right) // 2
            temp = mid*(mid+1) // 2
            if temp >= x:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        print(ans)
    else:
        x -= val
        ans = k
        main = ((k-1)*k) // 2

        if x >= main:
            print(2*k - 1)
            return
        
        left, right = 1, k - 1
        ans = k - 1

        while left <= right:
            mid = (left + right) // 2

            s = mid * k - mid * (mid + 1) // 2

            if s >= x:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        print(k + ans)
                                  
    


          
            
               
     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()