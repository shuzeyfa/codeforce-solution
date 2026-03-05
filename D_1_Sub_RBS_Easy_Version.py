
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

    stack = []

    ans = 0

    for i in range(n):
        if s[i] == "(":
            stack.append("(")
        else:
            stack.pop()
        ans = max(ans, len(stack))
    
    first = 0

    for i in range(n):
        if s[i] == ")":
            break
        first += 1
    if first >= ans:
        print(-1)
        return

    res = []
    stack = []
    count = 0
    i = 0
    while len(res) < ans:
        if s[i] == ")":
            res.pop()
            count += 1
        else:
            res.append("(")
        i += 1
    
    while i < n:
        res.append(s[i])
        i += 1
    
    print(len(res))
    
    





                                  
    


          
            
               
     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()