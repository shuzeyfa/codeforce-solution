
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
    
    
@lru_cache(None)    
def dp(ind, s):
    
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

# ====================== SEGMENT TREE TEMPLATE (SUM) ======================
class SegmentTree:
    def __init__(self, n, arr):
        self.n = n
        self.tree = [0] * (4 * n)
        self.build(1, 0, n-1, arr)
    
    def build(self, node, start, end, arr):
        if start == end:
            self.tree[node] = arr[start]
            return
        mid = (start + end) // 2
        self.build(2*node, start, mid, arr)
        self.build(2*node+1, mid+1, end, arr)
        self.tree[node] = self.tree[2*node] + self.tree[2*node+1]
    
    # Change arr[idx] = val
    def update(self, node, start, end, idx, val):
        if start == end:
            self.tree[node] = val
            return
        mid = (start + end) // 2
        if idx <= mid:
            self.update(2*node, start, mid, idx, val)
        else:
            self.update(2*node+1, mid+1, end, idx, val)
        self.tree[node] = self.tree[2*node] + self.tree[2*node+1]
    
    # Sum from l to r (0-based indices)
    def query(self, node, start, end, l, r):
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        return self.query(2*node, start, mid, l, r) + \
               self.query(2*node+1, mid+1, end, l, r)

"""
we can use it like this 

1 - To build

    st = SegmentTree(n, arr)

2 - update 
    st.update(1, 0, n-1, idx, val)

3 - query
    print(st.query(1, 0, n-1, l, r))

"""





        
          
def solve():
    n, qk = map(int, input().split())
    l = list(map(int,input().split()))
    q = list(map(int,input().split()))
 
    d = defaultdict(int)
    pre = [l[0]]
 
    for i in range(1,n):
        pre.append(pre[i-1] + l[i])
 
    val = 0
    for i in range(n):
        val = max(val, l[i])
        d[val] = i
    
    ans = []
    key = list(d.keys())
    key.sort()
 
    for i in range(qk):
        val = bisect_right(key, q[i])
        if val == 0:
            ans.append(0)
        else:
            ind = key[val-1]
            val = d[ind]
            ans.append(pre[val])
    print(*ans)      
     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()