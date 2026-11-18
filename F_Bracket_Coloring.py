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
    n = getInt()
    s = getStr()
    
    if s.count('(') != s.count(')'):
        print(-1)
        return
    
    ans = [0]*n
    stack = []
    
    count = 0
    
    for i in range(n):
        if s[i] == '(':
            if count > 0:
                ans[i] = 2
                count -= 1
            else:
                
                stack.append(i)
        else:
            if stack:
                ind = stack.pop()
                ans[ind] = 1
                ans[i] = 1
            else:
                ans[i] = 2
                count += 1
    # print(stack)
    for i in stack:
        if count > 0:
            count -= 1
            ans[i] = 2
            continue
        ans[i] = 1
    k = len(set(ans))
    if k == 1:
        print(1)
        ans = [1]*n
        print(*ans)
    else:
        print(k)
        print(*ans)
    
        
      
             
    
for _ in range(t):
    solve()