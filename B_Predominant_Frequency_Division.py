
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
    
    
    one = two = three = 0
    count1 = [0] * n
    count2 = [0] * n
    
    for ind in range(n):
        if l[ind] == 1:
            one += 1
        elif l[ind] == 2:
            two += 1
        else:
            three += 1
        
        count1[ind] = one - (two + three)    
        count2[ind] = (one + two) - three       
    
    suf_max = [0] * (n - 1)
    suf_max[n - 2] = count2[n - 2]
    for j in range(n - 3, -1, -1):
        if count2[j] > suf_max[j + 1]:
            suf_max[j] = count2[j] 
        else:
            suf_max[j] = suf_max[j + 1]
    
    check = False
    for ind in range(0, n - 2):   
        if count1[ind] >= 0:
            if suf_max[ind + 1] >= count2[ind]:
                check = True
                break
    
    if check:
        print("YES")
    else:
        print("NO") 
        
                     
    
                      
    
for _ in range(t):
    solve()