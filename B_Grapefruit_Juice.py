
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
    n, k, p = getIntList()
    l = getIntList()
    
    l.sort()
    
    ind = 0
    ans = 0
    
    while ind < n:
        
        if ind+k > n:
            break
        
        temp = ind
        val = 0
        for i in range(k):
            val += l[temp]
            temp += 1
        
        if val <= p:
            ans += p
            ind = temp
        else:
            break
    
    for i in range(ind, n):
        ans += l[i]
    print(ans)
            

          
            
               
     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()