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

t = getInt()

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
    
    
        
                
def solve():
    n = int(input())
    a = getIntList()
    b=getIntList()
    
    b.sort(reverse=True)
    a.sort()
    
    val = []
    count = 0
    i, j = n-1, 0
    while j<n and i >= 0:
        while i >= 0 and a[i] > b[j]:
            i -= 1
            count += 1
        val.append(count)
        j += 1
    rem = n - len(val)
    for i in range(rem):
        val.append(count)        
    
    final = 1
    for i in range(n):
        val2 = val[i]
        val2 -= i
        
        if val2 <= 0:
            final = 0
            break
        final = (final * val2) % (10**9 +7)  
             
    
    print(final) 
                 
          
         
                
    
                      
    
for _ in range(t):
    solve()
    
    