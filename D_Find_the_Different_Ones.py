
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
    
    dif = [0]
    
    for i in range(1, n):
        if l[i] != l[i-1]:
            dif.append(i)
        else:
            dif.append(dif[-1])
    # print(dif)
    ind = [0]
    
    for i in range(1, n):
        if l[i] != l[i-1]:
            ind.append(i)
    # print(ind)
    
    for i in range(getInt()):
        left, right = getIntList()
        
        index = dif[left-1]
        place_of_index_in_ind = bisect_left(ind, index)
        if place_of_index_in_ind+1 == len(ind) or ind[place_of_index_in_ind+1] >= right:
            print(-1, -1)
        else:
            print(left, ind[place_of_index_in_ind+1]+1)
        
    print()
    


          
            
               
     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()