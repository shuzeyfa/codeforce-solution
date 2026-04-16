
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

    d = defaultdict(list)

    for i in range(n):
        if l[i] not in d:
            d[l[i]].append(0)
        d[l[i]].append(i+1)

    for i in d:
        d[i].append(n+1)
    
    
    maxGap = defaultdict(int)

    for i in d:
        temp = d[i]

        maxx = 1
        for j in range(1, len(temp)):
            maxx = max(maxx, temp[j] - temp[j-1])
        
        maxGap[i] = maxx
    
    ans = [float('inf')]*n

    for i in maxGap:
        ans[maxGap[i] - 1] = min(ans[maxGap[i] - 1], i)
    
    minVal = float('inf')
    for i in range(n):
        ans[i] = min(minVal, ans[i])
        minVal = min(minVal, ans[i])
    
    for i in range(n):
        if ans[i] == float('inf'):
            ans[i] = -1
    print(*ans)
        
                                  
    


          
            
               
     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()