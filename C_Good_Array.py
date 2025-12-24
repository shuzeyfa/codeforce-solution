
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
    n = getInt()
    l = getIntList()

    s = set()
    original = l[:]

    summ = sum(l)
    l.sort()

    for i in range(n):
        if l[i] in s:
            continue
        rem = summ - l[i] 
        if l[i] == l[-1]:
            another = l[-2]
        else:
            another = l[-1]
        
        if rem - another == another:
            s.add(l[i])
    
    ans = []
    # print(s)

    for i in range(n):
        if original[i] in s:
            ans.append(i+1)
    if len(ans) == 0:
        print(0)
        return

    print(len(ans))
    print(*ans)

                                  
    


          
            
               
     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()