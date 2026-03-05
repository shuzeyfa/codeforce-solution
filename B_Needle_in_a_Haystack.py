
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
    s = getStr()
    t = getStr()

    d2 = Counter(s)

    d = Counter(t)

    for i in d2:
        if d[i] < d2[i]:
            print("Impossible")
            return

    value = []
    for i in d:
        val = d[i]
        val -= d2[i]

        for j in range(val):
            value.append(i)

    ans = []

    value.sort()

    i = 0
    j = 0
    print(value)

    while i < len(value) and j < len(s):
        if s[j] < value[i]:
            ans.append(s[j])
            j += 1
        else:
            ans.append(value[i])
            i += 1
    
    while j < len(s):
        ans.append(s[j])
        j += 1
    
    while i < len(value):
        ans.append(value[i])
        i += 1
    
    print("".join(ans))
                                  
    


          
            
               
     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()