
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
    l = getIntList()

    check = [True]*n
    check[0] = False

    for i in range(1, n):
        val = l[i-1] // 2 + 1
        if l[i] < val:
            check[i] = False

    ind = 0
    ans = 0

    while ind < n:
        
        count = 1
        ind += 1

        while ind < n and check[ind]:
            count += 1
            ind += 1
        
        if count == k+1:
            ans += 1
            continue
        add = count - k
        if add > 0:
            ans += add

    print(ans) 
    # print(check)                             
    


          
            
               
     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()