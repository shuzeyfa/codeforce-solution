
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

    left, right = 0, n - 1

    for i in range(n):

        expected = 'a' if i%2 == 0 else 'b'

        if s[left] == expected or s[left] == '?':
            left += 1
        elif s[right] == expected or s[right] == '?':
            right -= 1
        else:
            print("NO")
            return
    
    print("YES")
    

    


          
            
               
     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()