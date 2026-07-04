
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
    
    s = getStr()
    
    count = 0
    
    i = 0
    while i < n:
        
        char = s[i]
        while i < n and char == s[i]:
            i += 1
        count += 1
        
    if s[0] == s[-1]:
        print(1)
    else:
        if count < 3:
            print(2)
        else:
            print(1)
     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()