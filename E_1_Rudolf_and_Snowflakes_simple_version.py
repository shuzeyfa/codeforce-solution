
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
    if n <= 6:
        print("NO")
        return


    x = 2

    while x*x <= n:

        summ = 1
        multiplier = 1

        while summ < n:
            multiplier *= x
            summ += multiplier

            if summ == n:
                print("YES")
                return
        x += 1
    print("NO")


                                  
    


          
            
               
     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()