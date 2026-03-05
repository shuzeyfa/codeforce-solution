
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
    s = getStr()
    ans = []
    get = False

    for i in range(len(s)):
        if s[i] == "0" and not get:
            get = True
        else:
            ans.append(s[i])
    
    if not get and len(ans) > 0:
        ans.pop()
    
    ans.reverse()

    while len(ans) > 0 and ans[-1] == "0":
        ans.pop()
    ans.reverse()

    print("".join(ans))
                                  
    


          
            
               
     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()