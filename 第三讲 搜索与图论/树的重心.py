def add(a, b):
    global idx
    e[idx] = b
    ne[idx] = h[a]
    h[a] = idx
    idx += 1

def dfs(u):
    global ans
    # print(u)
    sum = 1
    res = 0
    i = h[u]
    while i != -1:
        j = e[i]
        if st[j]:
            st[j] = False
            s = dfs(j)
            res = max(res, s)
            sum += s
        i = ne[i]
    res = max(n-sum, res)
    ans = min(ans, res)
    return sum

if __name__ == '__main__':
    N = int(1e6 + 10)
    n = int(input())
    h = [-1]*(n+1)
    e = [0]*N
    ne = [0]*N
    idx = 0
    st = [True]*(n+1)
    st[1] = False
    for _ in range(n-1):
        a, b = list(map(int, input().split()))
        # print(a, b)
        add(a, b)
        add(b, a)
    ans = n
    dfs(1)
    print(ans)