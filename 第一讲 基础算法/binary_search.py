n, k = list(map(int, input().split()))
q = list(map(int, input().split()))
for _ in range(k):
    key = int(input())
    l, r = 0, n - 1
    while l < r:
        m = (l + r) // 2
        if q[m] >= key:
            r = m
        else:
            l = m+1

    if q[l] != key:
        print("-1 -1")
    else:
        print(f"{l}", end=' ')
        l, r = 0, n - 1
        while l < r:
            m = (l + r +1) // 2
            if q[m] <= key:
                l = m
            else:
                r = m-1
        print(f"{l}")