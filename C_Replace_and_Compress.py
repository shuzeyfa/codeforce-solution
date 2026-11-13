import sys, os
import math, heapq
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
    s = getStr()
    n = len(s)

    count = 1
    for i in range(n - 1):
        if s[i] != s[i + 1]:
            count += 1

    sett = {count}


    for i in range(1, n - 1):
        if s[i] == "0":
            change = "1"
        else:
            change = '0'
        
        
        val = 0
        prev_left = (s[i - 1] != s[i])
        curleft = (s[i - 1] != change)

        if curleft != prev_left:
            if curleft:
                val += 1 
            else:
                val -= 1

        prev_right = (s[i] != s[i + 1])
        curRight = (change != s[i + 1])

        if curRight != prev_right:
            if curRight:
                val += 1 
            else:
                val -= 1

        sett.add(count + val)

    
    print(len(sett))
      
             
    
for _ in range(t):
    solve()