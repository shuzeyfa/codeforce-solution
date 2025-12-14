
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
    n, m = getIntList()
    l = getIntList()
    l.sort()

    def check(val):

        ans = 0
        ind = 0

        while ind < m:
            count = 0
            temp = l[ind]

            while ind < m and l[ind] == temp and count < val:
                count += 1
                ind += 1
            if count >= val:
                ans += 1
        return ans >= n

    
    left, right = 1, m
    ans = 0
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