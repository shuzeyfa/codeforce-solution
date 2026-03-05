import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    freq = {}
    for x in arr:
        freq[x] = freq.get(x, 0) + 1

    x = y = z = 0
    for cnt in freq.values():
        if cnt % 2 == 1:
            x += 1                 # odd frequency
        elif cnt % 4 == 2:
            y += 1                 # cnt ≡ 2 (mod 4)
        else:
            z += 1                 # cnt ≡ 0 (mod 4)

    # theoretical maximum
    ans = x + 2*y + 2*z

    # bad case: x == 0 and z is odd
    if x == 0 and z % 2 == 1:
        ans -= 2

    print(ans)
