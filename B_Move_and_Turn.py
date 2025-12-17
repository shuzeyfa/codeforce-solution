
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

    vertical = set()
    horizontal = set()

    vertical.add((0, -1))
    vertical.add((0, 1))

    horizontal.add((1, 0))
    horizontal.add((-1, 0))

    for i in range(2, n+1):

        new_vert = set()
        new_hor = set()

        for x, y in vertical:
            new_hor.add((x+1, y))
            new_hor.add((x-1, y))
        
        for x, y in horizontal:
            new_vert.add((x, y+1))
            new_vert.add((x, y-1))
        
        vertical = new_vert
        horizontal = new_hor
    
    print(len(vertical | horizontal))
                                  
    


          
            
               
     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()