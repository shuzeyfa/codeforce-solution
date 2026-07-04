
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
    n, m = getIntList()

    l = getIntList()
    b = getIntList()
    even = []
    odd = []
    for i in range(n):
        if i%2 == 0:
            odd.append(l[i])
        else:
            even.append(l[i])
    
    odd.sort(reverse=True)
    even.sort(reverse=True)
    
    oddOperation = evenOperation = 0
    
    summ = 0
    for i in range(m):
        if b[i]%2 == 1:
            oddOperation += 1
        else:
            evenOperation += 1
    
    if oddOperation > 0:
        if odd[0] >= 0:
            for i in range(min(oddOperation, len(odd))):
                if odd[i] < 0:
                    break
                summ += odd[i]
        else:
            summ += odd[0]
    
    if evenOperation > 0:
        if even[0] >= 0:
            for i in range(min(evenOperation, len(even))):
                if even[i] < 0:
                    break
                summ += even[i]
        else:
            summ += even[0]
    
    
    print(sum(l) - summ)
    
    
          
            
               
     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()