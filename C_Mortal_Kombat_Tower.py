
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

sys.setrecursionlimit( 2 * 10 ** 5 + 1)

t = 1
t = getInt()

   
          
def solve():
    n = getInt()
    l = getIntList()

    @lru_cache(None)
    def dp(ind):

        if ind >= n:
            return 0
        
        if l[ind] == 1:
            ans = 1
        else:
            ans = 0

        first = dp(ind + 2)
        sec = dp(ind + 3)

        third = fourth = float('inf')

        ans2 = 0

        if ind+1 < n:
            if l[ind+1] == 1:
                ans2 = ans + 1
            else:
                ans2 = ans 
            
            third = dp(ind + 3)
            fourth = dp(ind + 4)

        return min(first+ans, sec+ans, third+ans2, fourth+ans2)

                                  
    
    print(dp(0))

          
            
               
     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()