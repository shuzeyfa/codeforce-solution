import sys

qrTNum = int(sys.stdin.readline())

for _ in range(qrTNum):
    x, y, k = map(int, sys.stdin.readline().split())

    d = y - x
    ans = 0

    while k > 0 and x <= d:
        ans += d % x
        x += 1
        k -= 1

    ans += d * k

    print(ans)