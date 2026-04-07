
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

def count_divisors(n):
    if n <= 0:
        return 0
    
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if i * i == n:
                count += 1          
            else:
                count += 2        
    return count
          
def solve():
    x ,y =getIntList()

    dif = abs(x - y)   
    if dif == 1:
        print(1)
        ans = [-1]*y
        ans += [1]*x
        print(*ans)
        return

    count = count_divisors(dif)
    print(max(count, 1) %   676767677)
    ans = [-1]*y
    ans += [1]*x
    print(*ans)


          
            
               
     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()