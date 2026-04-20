
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
    n, k =getIntList()
    s = getStr()

    rank = [0]*n
    parent = {i:i for i in range(n)}

    def find(x):
        while x != parent[x]:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x,y):
        rep1 = find(x)
        rep2 = find(y)
        if rep1 != rep2:
            if rank[rep1] > rank[rep2]:
                parent[rep2] = rep1
            elif rank[rep2] > rank[rep1]:
                parent[rep1] = rep2
            else:
                if rep1 <= rep2:
                    parent[rep2] = rep1
                    rank[rep1] += 1
                else:
                    parent[rep1] = rep2
                    rank[rep2] += 1


    for i in range(n // 2):

        u, v = i, n - i - 1
        union(u, v)

    for i in range(n - k):
        u, v = i, i+k
        union(u, v)
    
    d = defaultdict(Counter)

    for i in range(n):
        par = find(i)

        d[par][s[i]] += 1
    
    ans = 0

    for group in d:
        total = 0
        maxx = 0

        for ch in d[group]:
            cnt = d[group][ch]
            total += cnt
            maxx = max(maxx, cnt)

        ans += total - maxx
    print(ans)

                                  
    


                   
     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()