
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

    if l[-1] == 1 or l[0] == 1:
        print("Alice")
        return

    if len(set(l)) == 1 and l[0] == 1:
        print("Alice")
        return

    if len(set(l)) == 1 and l[0] == 0:
        print("Bob")
        return
    
    if l.count(1) == 1:
        print("Bob")
        return
    
    check = False

    for i in range(n):
        if l[i] == 1:
            if check:
                print("Bob")
                return
            else:
                check = True
    print("Alice")
                                  
    


          
            
               
     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()