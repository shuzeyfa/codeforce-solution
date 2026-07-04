
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
    s = getIntList()
    
    d = Counter(s)
    
    l = list(set(s))
    l.sort()
    
    for i in range(len(l)-1, -1, -1):
        
        if (d[l[i]])%2 == 0:
            print("YES")
            return
        else:
            if i > 0:
                if (l[i]-l[i-1]) <= k:
                    print("YES")
                    return
    print("NO")
    
        
        
                     
    
                      
    
for _ in range(t):
    solve()