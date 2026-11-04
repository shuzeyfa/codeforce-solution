import sys, os
import math, heapq
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


def solve():
    n, m = getIntList()
    g = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, w = getIntList()
        g[a].append((b, w))
        g[b].append((a, w))
    
    INF = 10**18
    dist = [INF] * (n + 1)
    prev = [-1] * (n + 1)
    dist[1] = 0
    pq = [(0, 1)]
    
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in g[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                prev[v] = u
                heapq.heappush(pq, (nd, v))
    
    if dist[n] == INF:
        print(-1)
        return
    
    path = []
    cur = n
    while cur != -1:
        path.append(cur)
        cur = prev[cur]
    path.reverse()
    print(*path)


t = 1
# t = getInt()
for _ in range(t):
    solve()