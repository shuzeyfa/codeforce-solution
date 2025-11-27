
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


def xor(n):
    if n%4 == 0:
        return n
    elif n%4 == 1:
        return 1
    elif n%4 == 2:
        return n+1
    else:
        return 0
        
        
     
def longestcommonsubstring(s1, s2):
    
    maxlen = 0
    end = 0
    
    n, m = len(s1), len(s2)
    dp = [[0]*(m+1) for i in range(n+1)]
    
    for i in range(1,n+1):
        for j in range(1, m+1):
            if s1[i-1]==s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                if dp[i][j] > maxlen:
                    maxlen = dp[i][j]
                    end = i
    
    print(s1[end-maxlen:end])
    return maxlen                
    

def prime_numbers(n):
    prime = [True]*(n+1)
    prime[0] = False
    prime[1] = False
    for i in range(3, int(math.sqrt(n))+1 , 2):
        if prime[i]:
            for j in range(i*i, n+1, i):
                prime[j] =False
    
    primes_num = [2] + [i for i in range(3, n+1, 2) if prime[i] == True]
    return primes_num
    
    
@lru_cache(None)    
def dp(ind, s):
    n = 2
    if ind + 1 ==  n:
        ans += 1
        return 
    if ind + 2 == n:
        if s[ind] == s[ind+1]:
            ans += 1
            return 
        else:
            ans += 2
            return  
             
    if s[ind] == s[ind+1]:
        return dp(ind+1, s) + 1
    return dp(ind+1, s) + dp(ind+2, s) + 2     
        
       
def solve():
    n, d = getIntList()
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
                rank[rep1] += rank[rep2] + 1
            elif rank[rep2] > rank[rep1]:
                parent[rep1] = rep2
                rank[rep2] += rank[rep1] + 1
            else:
                if rep1 <= rep2:
                    parent[rep2] = rep1
                    rank[rep1] += rank[rep2] + 1
                else:
                    parent[rep1] = rep2
                    rank[rep2] += rank[rep1] + 1

    # print(rank)
    maxx = 1
    for i in range(d):
        u, v = getIntList()
        union(u-1, v-1)
        print(rank)
        par = find(i)
        maxx = max(maxx, rank[par])
        print(maxx)  





        
    


    



                                  
    


          
            
               
     
                             
    
        
                     
    
t = 1               
# t = getInt()
    
for _ in range(t):
    solve()
    