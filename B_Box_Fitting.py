
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

    ans = 0

    d = defaultdict(int)

    for i in l:
        val = int(math.log2(i))
        d[val] += 1

    t = True
    while t:
        value = k

        checked = False
        for i in range(20, -1, -1):
            if d[i] == 0:
                continue

            num = 2 ** i
            while value >= num and d[i] > 0:
                d[i] -= 1
                value -= num
                checked = True
        if not checked:
            break
        ans += 1
    print(ans)                                
    


          
            
               
     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()