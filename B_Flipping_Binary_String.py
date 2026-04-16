
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
    s = getStr()

    num1 = s.count("1")
    if num1 == 0:
        print(0)
        return

    num0 = n - num1

    if num1 % 2 == 0:
        ops = [i + 1 for i in range(n) if s[i] == "1"]
        print(len(ops))
        print(*ops)
    elif num0 % 2 == 1:
        ops = [i + 1 for i in range(n) if s[i] == "0"]
        print(len(ops))
        print(*ops)
    else:
        print(-1)
                                  
    


          
            
               
     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()