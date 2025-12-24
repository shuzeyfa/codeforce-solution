
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
    n  = getInt()

    if n%2 == 0:
        print(n//2, n//2)
        return
    
    def find(val):

        div = 3
        while div*div <= n+1:
            if n%div == 0:
                return div
            div += 2
        return val

    small = find(n)
    if small == n:
        print(1, n-1)
    else:
        left = n // small
        right = n - left
        print(left, right)

          
            
               
     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()