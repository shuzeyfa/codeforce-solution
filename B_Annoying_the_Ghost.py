
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
    
    b = getIntList()
    
    taken = [False]*n
    
    ind = []
    
    for i in range(n):
        
        get = False
        for j in range(n):
            if b[j] >= l[i] and not taken[j]:
                get = True
                ind.append(j)
                taken[j] = True
                break
        if not get:
            print(-1)
            return
    
    ans = 0
    val = n - 1
    # print(ind)
    
    while val >= 0:
        
        index = ind.index(val)
        while index != val:
            ind[index], ind[index+1] = ind[index+1], ind[index]
            index += 1
            ans += 1
        val -= 1
    print(ans)
    # print(ind)       
    
              
               
     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()