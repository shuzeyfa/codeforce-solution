
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
    n, k = getIntList()
    a = getIntList()
    h = getIntList()

    ans = 0
    left = 0
    curr_sum = 0

    for right in range(n):
        curr_sum += a[right]

        if right > 0 and h[right-1] % h[right] != 0:
            left = right
            curr_sum = a[right]

        while curr_sum > k:
            curr_sum -= a[left]
            left += 1

        ans = max(ans, right - left + 1)

    print(ans)
 



          
            
               
     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()