t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    a = list(map(int, input().split()))
 
    pos = [0] * (n + 1)
    for i in range(n):
        pos[p[i]] = i
 
    ok = True
    for i in range(1, n):
        if a[i] != a[i-1]:
            if pos[a[i]] < pos[a[i-1]]:
                ok = False
                break
    if ok:
        print("YES")
    else:
        print("NO")