
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

    ans = [l[0]]

    dec = True if l[1] < l[0] else False

    ind = 1

    while ind < n:

        if dec:
            while ind < n and l[ind] < l[ind-1]:
                ind += 1
                
            ans.append(l[ind-1])
            dec = not dec   
        else:
            while ind < n and l[ind] > l[ind-1]:
                ind += 1
                
            ans.append(l[ind-1])
            dec = not dec   

    print(len(ans))   
    print(*ans)              
    


          
            
               
     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()