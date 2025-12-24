
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

    if n < 24:
        print("NO")
        return

    def fact(num):
        
        d = defaultdict(int)

        div = 2

        while div*div <= num:

            while num%div == 0:
                d[div] += 1
                num //= div
            div += 1
        if len(d) == 0:
            return [-1, -1]
        if len(d) == 1:
            for i in d:
                if d[i] == 1:
                    return [-1, -1]
                else:
                    return [i, i*i]
        
        ans = []
        for i in d:
            ans.append(i)
            if len(ans) == 2:
                return ans
    

    first, second = fact(n)    
    if first == -1:
        print("NO")
        return 
    
    third = n // (first*second)

    if first*second*third > n or first*second*third < n or second <= 1 or first <= 1 or third <= 1 or first == second or second == third or third == first:
        print("NO")
        return
    print("YES")
    print(first, second, third)
    
                                  
    


          
            
               
     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()