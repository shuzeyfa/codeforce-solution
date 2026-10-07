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
    
    if n == 3:
        if l[0] < l[1] and l[2] < l[1]:
            print("YES")
        else:
            print("NO")
        return
    
    first = []
    sec = []
    
    for i in range(0, n, 2):
        first.append(l[i])
    
    for i in range(1, n, 2):
        sec.append(l[i])
        
    first.sort()
    sec.sort()
    
   
    
    ans = []
    
    for i in range(min(len(first), len(sec))):
        ans.append(first[i])
        ans.append(sec[i])
    if len(first) > len(sec):
        ans.append(first[-1])
    
    if ans[-1] == n:
        ans[-1], ans[-3] = ans[-3], ans[-1]
    
    if ans[-3] == n:
        ind = n - 3
    else:
        ind = n - 2
        
    print(ans)
    for i in range(1, ind+1):
        if ans[i] < ans[i-1]:
            print("NO")
            return
    
    for i in range(ind, n-1):
        if ans[i] < ans[i+1]:
            print("NO")
            return
    print("YES")
    
    # if n in first and n%2 == 1:
    #     first.pop(-1)
    #     sec.pop(-1)
    # elif n in first and n%2 == 0:
    #     sec.pop(-1)
    # elif n in sec and n%2 == 1:
    #     sec.pop(-1)
    # else:
    #     first.pop(-1)
    #     sec.pop(-1)
    
    # ans = []
    # print(first)
    # print(sec)
    # for i in range(min(len(first), len(sec))):
    #     ans.append(first[i])
    #     ans.append(sec[i])
    # if len(first) > len(sec):
    #     ans.append(first[-1])
    
    # for i in range(1, len(ans)):
    #     if ans[i] <= ans[i-1]:
    #         print("NO")
    #         return
    # print("YES")
        


for _ in range(t):
    solve()