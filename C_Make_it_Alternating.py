
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
    s = getStr()

    fact = 0

    mul = 1

    ind = 0
    mod =  998244353

    while ind < len(s):

        val = s[ind]
        count = 0

        while ind < len(s) and s[ind] == val:
            count += 1
            ind += 1
        
        mul = (mul * (count%mod)) % mod
        fact += count - 1
    
    ans = 1

    for i in range(2, fact+1):
        ans = (ans * (i%mod)) % mod
    print(fact, (ans * mul) % mod)



       
                                  
    


          
            
               
     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()