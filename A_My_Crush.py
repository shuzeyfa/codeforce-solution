
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
    n, m, k = getIntList()
    l = getIntList()

    left, right = m-2, m
    count = 1

    while left >= 0 or right < n:
        if left >= 0 and (l[left] != 0 and l[left] <= k):
            print(count*10)
            return
        if right < n and (l[right] > 0 and l[right] <= k):
            print(count*10)
            return
        right += 1
        left -= 1
        count += 1

    
                                  
    


          
            
               
     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()