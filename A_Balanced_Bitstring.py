
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
    n, k = getIntList()
    s = getStr()

    l = [-1]*k


    for i in range(n):
        if s[i] == '?':
            continue

        if l[i%k] != -1:
            if l[i%k] != int(s[i]):
                print("NO")
                return
        else:
            l[i%k] = int(s[i])

    one, zero = l.count(1), l.count(0)

    if one > k//2 or zero > k//2:
        print("NO")
        return

    print("YES")               
    


          
            
               
     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()