
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

def digit(n):
    return sum(int(d) for d in str(n))
          
def solve():
    x = getInt()

    count = 0

    for i in range(1, 201):

        y = x + i

        if i == digit(y):
            count += 1
    
    print(count)
                                  
    


          
            
               
     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()