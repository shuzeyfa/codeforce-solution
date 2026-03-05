
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

    d = defaultdict(int)
    for i in l:
        d[i] += 1

    res = []
    for i in d:
        res.append(d[i])

    res.sort(reverse=True)

    val = res[0] - 1
    # print(res)
    ans = res[0]
    # print(ans)

    for i in range(1, len(res)):
        ans += min(val, res[i])
        val  = min(val-1, res[i]-1)
        if val < 0:
            val = 0
        
               
    print(ans)                           
    


          
            
               
     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()