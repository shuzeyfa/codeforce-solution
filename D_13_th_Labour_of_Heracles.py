
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
    w = getIntList()

    d = defaultdict(int)

    for i in range(n-1):
        u, v = getIntList()
        d[u] += 1
        d[v] += 1
    
    ans = []

    d2 = defaultdict(int)
    # print(d)
    for i in d:
        val = (d[i] - 1) 
        ans += ([w[i-1]] * val)
    
    ans.sort(reverse=True)
    summ = sum(w)
    # print(ans)
    print(summ, end= " ")
    for i in range(n-2):
        summ += ans[i]
        print(summ, end=" ")
    print()



                                  
    


          
            
               
     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()