
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

sys.setrecursionlimit(4000)


t = 1
t = getInt()

   
          
def solve():
    n = getInt()
    l = getIntList()
    s = getStr()

    d = defaultdict(list)

    for i in range(n-1):
        d[l[i]].append(i+2)

    ans = 0

    def dfs(par):
        nonlocal ans

        black = white = 0

        for child in d[par]:

            w, b = dfs(child)

            white += w
            black += b
        
        if s[par-1] == "W":
            white += 1
        else:
            black += 1

        if white == black:
            ans += 1
        
        return white, black


    dfs(1)   
    print(ans)                               
    


          
            
               
     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()