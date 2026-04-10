
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

    l = []
    for i in range(n):
        l.append(getStr())

    
    indegree = [0]*26
    d = defaultdict(list)

    possible = True

    for i in range(n-1):

        prev, current = l[i], l[i+1]

        get = False

        for j in range(min(len(prev), len(current))):
            if prev[j] != current[j]:
                
                d[prev[j]].append(current[j])
                indegree[  ord(current[j]) - ord("a")  ] += 1

                get = True
                break
        
        if not get and len(prev) > len(current):
            possible = False
            break
    
    if not possible:
        print("Impossible")
    else:

        q = deque()
        # print(d)
        

        for i in range(26):
            if indegree[i] == 0:
                q.append(chr(i + ord("a")))
        # print(q)
        ans = []
        
        while q:

            cur = q.popleft()

            ans.append(cur)

            for i in d[cur]:

                indegree[  ord(i) - ord("a")  ] -= 1
                if indegree[  ord(i) - ord("a")  ] == 0:
                    q.append(i)

        if len(ans) == 26:
            print("".join(ans))
        else:
            print("Impossible")

                                            
            
    
    


          
            
               
     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()