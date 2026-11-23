
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
    
    x, y, m = getIntList()
    s = getStr()
    
    
    
    @lru_cache(None)
    def dfs(i, a, b):
        
        
        res = a+b

        if i == m or a+b == 0:
            return res

        if s[i] == '+':
            if a > 0:
                res = max(res, dfs(i+1, a-1, b+1))
            if b > 0:
                res = max(res, dfs(i + 1, a, b + 1))
        else:
            if a > 0:
                res = max(res, dfs(i + 1, a - 1, b))
            if b > 0:
                res = max(res, dfs(i + 1, a + 1, b - 1))

        return res
    
    
    

    print(dfs(0, x, y))
        
                                  
    


          
            
               
     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()