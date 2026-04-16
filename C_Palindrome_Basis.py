
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




MOD = 10**9 + 7

pal = []
for i in range(1, 40001):
    s = str(i)
    if s == s[::-1]:
        pal.append(i)

# DP
dp = [0] * (40000 + 1)
dp[0] = 1

for p in pal:
    for j in range(p, 40000 + 1):
        dp[j] = (dp[j] + dp[j - p]) % MOD

t = 1
t = getInt()

# "Once upon a time in a  quaint little village, there lived a curious young boy named David. David was [...]" -> text
# # "you will be provided with a text delimeted by triple backticks, generate a suitable title for it ." -> instructions
# """use the following format for the output 
#   - Text: <text we want to title> 
#   - Title: <The generated title> """ -> """output 

# prompt = instruction + output + f"```{text}```""""
          
def solve():
    n = getInt()

    print(dp[n])     
                                  
    


          
            
               
     
                             
    
        
                     
    
                      
    
for _ in range(t):
    solve()