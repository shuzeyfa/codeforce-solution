
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
    n, m, q = getIntList()
    a = getIntList()
    b = getIntList()

    a.sort(reverse=True)
    b.sort(reverse=True)

    prea = [0]
    preb = [0]

    for i in range(n):
        prea.append(prea[-1] + a[i])
    for i in range(m):
        preb.append(preb[-1] + b[i])
    

    
    # print(prea)
    for i in range(q):
        x, y, z = getIntList()

        minn = max(0, z - y)
        maxx = min(x, z)

        if z == 0:
            print(0)
            continue


        left, right = minn, maxx

        ind = left

        while left <= right:

            mid = (left + right) // 2
            
            sum_mid =  prea[mid] + preb[z - mid] 
            sum_prev = -1
            if mid > minn:
                sum_prev = prea[mid - 1] + preb[z - (mid - 1)] if (mid - 1) <= n and (z - mid + 1) <= m else -1
            
            if sum_mid >= sum_prev:
                # Current is better or equal, try larger k
                ind = mid
                left = mid + 1
            else:
                # Previous is better, try smaller k
                right = mid - 1
        
        val = prea[ind] + preb[z - ind]
        print(val)


                                  
    


          
            
               
     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()