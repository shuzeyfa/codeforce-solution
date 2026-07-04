
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
    
    a = getIntList()
    b = getIntList()
    
    ind = 0
    
    while ind < n:
        
        maxx = b[ind] - a[ind]
        if maxx < 0:
            print("NO")
            return
        ind += 1
        if ind < n:
            a[ind] -= maxx
        # if ind < n and a[ind] > b[ind]:
        #     val = a[ind] - b[ind]
        #     if val > maxx:
        #         print("NO")
        #         return
        #     ind += 1
    print("YES")
     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()