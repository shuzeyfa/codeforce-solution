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
    
        
    r,s , p = getIntList()   
    summ = r+s+p

    if s >= p:
        print('R'*summ)
           
    elif p >= r:
        print('S'*summ)
    else:
        print('P'*summ) 
        
    # summ = r+s+p
    
    # d = defaultdict(int)
    # d['R'] = r
    # d['S'] = s
    # d['P'] = p
    
    # d2 = dict(sorted(d.items(), key=lambda x:x[1], reverse=True))
    # # print(d2)
    # d3 = {'R': 'P', 'S': 'R', 'P': 'S'}
    # ans = []
    
    # count = 0
    # for i in d2:
    #     if count == 2:
    #         break
    #     # ans.insert([d3[i]]*d2[i])
    #     for j in range(d2[i]):
    #         ans.append(d3[i])
    #     count += 1
    
    # if len(ans) < summ:
    #     rem = summ - len(ans)
    #     for i in range(rem):
    #         ans.append(ans[0])
    # print(''.join(ans))
    # print(ans + ['s']*0)
             
    
for _ in range(t):
    solve()