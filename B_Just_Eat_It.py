
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

    check = True

    for i in l:
        if i < 0:
            check = False
            break
    if check and l[0] != 0 and l[-1] != 0:
        print("YES")
        return

    summ = sum(l)

    maxx = float("-inf")
    count = 0

    for i in range(n-1):
        count += l[i]
        maxx = max(maxx, count)

        if count < 0:
            count = 0

        if maxx >= summ:
            print("NO")
            return
    
    maxx = float("-inf")
    count = 0

    for i in range(1, n):
        count += l[i]
        maxx = max(maxx, count)

        if count < 0:
            count = 0

        if maxx >= summ:
            print("NO")
            return
    print("YES")



                                  
    


          
            
               
     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()