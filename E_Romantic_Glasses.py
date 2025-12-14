
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

    if n == 1:
        print("NO")
        return

    if n == 2:
        if l[0] == l[1]:
            print("YES")
        else:
            print("NO")
        return

    odd = even = 0

    s = set()

    for i in range(n):
        if i%2 == 0:
            odd += l[i]
        else:
            even += l[i]

        if even == odd:
            print("YES")
            return
        rem = abs(odd - even)
        if rem in s:
            print("YES")
            return
        s.add(odd+even)
    print("NO")     
                                  
    


          
            
               
     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()