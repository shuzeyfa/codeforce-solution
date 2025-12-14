import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    freq = set(a)        # check membership
    count = {}           # how many times each number appears
    for x in a:
        count[x] = count.get(x, 0) + 1

    a.sort()
    ans = []

    for v in a:
        if v not in freq:
            continue

        step = v
        x = v
        ok = True

        while x <= k:
            if x not in count:
                ok = False
                break

            if x in freq:
                freq.remove(x)

            x += step

        if not ok:
            print(-1)
            break

        ans.append(step)
    else:
        print(len(ans))
        print(*ans)
