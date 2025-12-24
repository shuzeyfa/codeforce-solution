
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
    n, k = getIntList()
    l = getIntList()

    left, right = 1, n

    def check(num):
        arr = l[:num]
        arr.sort()
        summ = 0
        
        ind = len(arr) - 1

        while ind >= 0:
            summ += arr[ind]
            ind -= 2
        return summ <= k

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