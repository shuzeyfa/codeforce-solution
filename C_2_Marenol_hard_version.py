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
    
    a = getStr()
    b = getStr()
    
    one = two = 0
    three = four = 0
    
    for i in range(0, n, 2):
        
        one += int(a[i])
        three += int(b[i])
    
    for i in range(1, n, 2):
        
        two += int(a[i])
        four += int(b[i])
    
    if one != three or two != four:
        print(-1)
        return
    
    ones = []
    twos = []
    threes = []
    fours = []
    
    count = 0
    for i in range(0, n, 2):
        
        if a[i] == "1":
            ones.append(count)
        if b[i] == "1":
            threes.append(count)
        count += 1
    
    count = 0
    for i in range(1, n, 2):
            
        if a[i] == "1":
            twos.append(count)
        if b[i] == "1":
            fours.append(count)
        
        count += 1
    
    ans = 0
    for i in range(len(ones)):
        ans += abs(ones[i] - threes[i])
    
    for i in range(len(twos)):
        ans += abs(twos[i] - fours[i])
    
    print(ans)
    # print(ones)
    # print(threes)
        
        
        


for _ in range(t):
    solve()