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


def count(leftList, rightList):
    inversion = 0
    i = j = 0
    
    merged = []
    
    while i < len(leftList) and j < len(rightList):
        if leftList[i] <= rightList[j]:
            merged.append(leftList[i])
            i += 1
        else:
            merged.append(rightList[j])
            j += 1
            inversion += len(leftList) - i
    
    merged += leftList[i:]
    merged += rightList[j:]
    
    return merged, inversion            

def merge(final):
    if len(final) <= 1:
        return final, 0
        
    mid = len(final) // 2
    left, left_inv = merge(final[:mid])
    right, right_inv = merge(final[mid:])
    
    merged, inv_merge = count(left, right)
    return merged, left_inv + right_inv + inv_merge     
          
def solve():
    n = getInt()
    
    l = []
    
    for i in range(n):
        u, v = getIntList()
        l.append((u, v))
   
    
    l.sort(key=lambda x:(x[0], -x[1]))
    # print(l)
    
    value = []
    
    for i in l:
        value.append(i[1])
    
    # print(value)
        
             
    _, ans = merge(value)
    print(ans) 
    # print(_)   
    
    
    
      
             
    
for _ in range(t):
    solve()
