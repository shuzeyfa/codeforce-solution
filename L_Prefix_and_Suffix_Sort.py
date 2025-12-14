from collections import defaultdict
for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))

    s = l[:]
    s.sort()

    left, right = 0, n
    ans = n

    
    def check(val):
        val2 = l[:]
        val2[:val] = sorted(l[:val])
        val2[n-val:] = sorted(val2[n-val:])
        return val2 == s
        


    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            ans = mid 
            right = mid - 1
        else:
            left = mid + 1
    print(ans)
            
