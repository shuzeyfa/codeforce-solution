
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
    
    divisble = []
    two = []
    non = []
    three = []
    
    for i in l:
        if i%6 != 0:
            if i%2 == 0:
                two.append(i)
            else:
                if i%3 == 0:
                    three.append(i)
                else:
                    non.append(i)
                
        else:
            divisble.append(i)
            
    ans = divisble + three + non + two
    
    print(*ans)
    
    
    
    
            
               
     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()