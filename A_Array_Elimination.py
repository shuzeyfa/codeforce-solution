
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

    if len(set(l)) == 1 and l[0] == 0:
        for i in range(1, n+1):
            print(i, end = " ")
        print()
        return

    d = defaultdict(int)

    for i in range(31):

        for j in l:
            temp = (j & (1 << i))
            if temp > 0:
                d[i] += 1

    
    ans = 0
    # print(d)


    for i in range(31):
        if d[i] == 0:
            continue

        if ans == 0:
            ans = d[i]
        else:
            ans = math.gcd(ans, d[i])
            
    # print(d)
    res = []
    # print(ans, "here")
    val = 1

    while val*val <= ans:

        if ans%val == 0:
            res.append(val)
            if (ans // val) != val:
                res.append(ans // val)
        val += 1
    res.sort()
    print(*res)

                                  
    


          
            
               
     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()