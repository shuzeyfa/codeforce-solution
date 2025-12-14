
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

    first = [1]
    second = []

    for i in range(1, n):
        if l[i] == l[0]:
            first.append(i+1)
        else:
            second.append(i+1)
    
    
    if len(first) == n:
        print("NO")
        return
    
    print("YES")
    print(first[0], second[0])
    
    for i in range(1, len(second)):
        print(first[0], second[i])
    
    for i in range(1, len(first)):
        print(second[0], first[i])

                                  
    


          
            
               
     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()