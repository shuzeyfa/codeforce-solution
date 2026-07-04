
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
    
    s = getStr()
    
    best = 10 ** 9
    ans = None
    
    for left_del in range(k + 1):
        keep = [True]*n
        
        need = left_del
        for i in range(n):
            if need and s[i] == "(":
                keep[i] = False
                need -= 1
        
        need = k - left_del
        for i in range(n-1, -1, -1):
            if need and s[i] == ")":
                keep[i] = False
                need -= 1
        
        open_cnt = 0
        pairs = 0
        
        for i in range(n):
            if not keep[i]:
                continue
            
            if s[i] == "(":
                open_cnt += 1
            elif open_cnt:
                open_cnt -= 1
                pairs += 1
        
        if pairs < best:
            best = pairs
            ans = keep
    print("".join('0' if ans[i] else '1' for i in range(n)))    
               
     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()