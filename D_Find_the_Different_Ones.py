
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

    pre = []
    suf = []

    val = l[0]
    start = True
    ind = -1

    i = 0

    while i < n:
        
        if val == l[i] and start:
            pre.append(-1)
            i += 1
            ind = i 
        else:
            start = False
            val = l[i] 
            while i < n and val == l[i]:
                pre.append(ind)
                i += 1
            ind = i 
    
    i = n - 1
    start = True
    val = l[-1]
    ind = n + 1

    while i >= 0:
        
        if val == l[i] and start:
            suf.append(-1)
            ind -= 1
            i -= 1
        else:
            start = False
            val = l[i] 
            while i >= 0 and val == l[i]:
                suf.append(ind)
                i -= 1
            ind -= 1
        # print(ind)

    suf.reverse()
    # print(suf)


    q = getInt()
    for query in range(q):
        left, right = getIntList()
        if pre[right-1] != -1 and pre[right-1] >= left:
            print(pre[right-1], right)
        elif suf[left-1] != -1 and suf[left-1] <= right:
            print(left, suf[left-1])
        else:
            print(-1, -1)


    print()       

    


          
            
               
     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()