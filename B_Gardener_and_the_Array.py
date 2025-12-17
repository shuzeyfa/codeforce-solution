
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
    l = []

    d = defaultdict(int)

    for i in range(n):
        temp = getIntList()
        l.append(temp)
        for j in range(1, temp[0]+1):
            d[temp[j]] += 1
    
    for i in range(n):
        temp = l[i]
        t = True
        for j in range(1, temp[0]+1):
            if d[temp[j]] <= 1:
                t = False
                break
        if t:
            print("Yes")
            return
    print("No")

                                  
    


          
            
               
     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()