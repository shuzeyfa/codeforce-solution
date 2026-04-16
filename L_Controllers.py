
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
    n = getInt()
    s = getStr()

    c1 = s.count("+")
    c2 = n - c1

    for i in range(getInt()):
        a, b= getIntList()

        if c1 == c2:
            print("YES")
            continue

        if a == b:
            print("NO")
            continue

        

        gcd = math.gcd(a, b)

        aa, bb = a // gcd, b // gcd

        tot = bb * (c1 - c2)

        if abs(tot) % abs(aa - bb) != 0:
            print("NO")
            continue
        
        if tot < 0:
            if aa > bb:
                if abs(tot) // abs(aa - bb) > c1:
                    print("NO")
                else:
                    print("YES")
            else:
                if abs(tot) // abs(aa - bb) > c2:
                    print("NO")
                else:
                    print("YES")
        else:
            if aa > bb:
                if abs(tot) // abs(aa - bb) > c2:
                    print("NO")
                else:
                    print("YES")
            else:
                if abs(tot) // abs(aa - bb) > c1:
                    print("NO")
                else:
                    print("YES")



                                  
    


          
            
               
     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()