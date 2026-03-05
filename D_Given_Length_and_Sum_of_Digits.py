
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
# t = getInt()

   
          
def solve():
    a, b = getIntList()

    if b == 0:
        print("0 0" if a == 1 else "-1 -1")
        return

    if b < 1 or b > 9*a:
        print(-1, -1)
        return
    
    mul = b // 9
    rem = b % 9

    if rem == 0:
        rem = 9
        mul -= 1

    ans = ["0"]*a
    for i in range(mul):
        ans[i] = "9"
    ans[mul] = str(rem)

    maxx = "".join(ans)

    ans2 = ["0"]*a
    ind = -1
    for i in range(mul):
        ans2[ind] = "9"
        ind -= 1

    rem2 = rem - 1
    if abs(ind) == a:
        ans2[0] = str(rem)
    else:
        ans2[0] = "1"
        ans2[ind] = str(rem2)



    print("".join(ans2), maxx)

                                  
    


          
            
               
     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()