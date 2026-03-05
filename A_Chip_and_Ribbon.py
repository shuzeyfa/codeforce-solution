
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

    ans = 0

    val = [0]*n
    val[0] = 1

    for i in range(n):
        if i == 0:
            if l[0] > val[0]:
                ans += l[0] - val[0]
                val[0] = l[i]
        else:
            if val[i-1] >= l[i]:
                val[i] = l[i]
            else:
                val[i] = l[i]
                temp = l[i] - val[i]
                ans += temp
        print(val)
        print(ans)
    print(ans)
                                  
    


          
            
               
     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()