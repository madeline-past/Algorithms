def find(a):
    if s[a]!=a:
        s[a] = find(s[a])
    return s[a]

if __name__ == '__main__':

    n, m = list(map(int, input().split()))
    unsorted_g = [tuple(map(int, input().split())) for _ in range(m)]
    g = sorted(unsorted_g, key=lambda x: x[-1])

    s = [i for i in range(n+1)]
    res = 0
    cnt = 0
    for x, y, w in g:
        if find(x) == find(y):
            continue
        s[find(x)] = find(y)
        res += w
        cnt += 1
    
    if cnt != n-1:
        print("impossible")
    else:
        print(res)
