
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
    n, a, b = getIntList()
    
    val = b / 3
    
    if val < a:
        ans = (n // 3) * b
        remStu = n%3
        if a*remStu < b:
            ans += a*remStu
        else:
            ans += b
        print(ans)
    else:
        print(n*a) 
            
               
     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()