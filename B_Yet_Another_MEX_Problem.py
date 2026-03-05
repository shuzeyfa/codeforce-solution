
import sys, os
import math
from collections import defaultdict, deque, Counter
from functools import lru_cache
from heapq import heapify, heappop, heappush
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
    l = getIntList()

    heap = []

    for i in range(n - k +1):
        minn = [False]*k

        for j in range(k):
            if l[j+i] < k:
                minn[l[j+i]] = True
        check = False
        for ind in range(k):
            if not minn[ind]:
                check = True
                heap.append(ind)
                break
        if not check:
            heap.append(k)
    
    rem = n - k + 1
    # print(heap)
    res = 0
    if 0 in l:
        res = 1

    ans = []
    for i in heap:
        heappush(ans, -i)
    
    for i in range(rem):
        val = -heappop(ans)
        val -= 1
        heappush(ans, -val)
    val = -heappop(ans)
    print( max(res, val) )

                                  
    


          
            
               
     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()