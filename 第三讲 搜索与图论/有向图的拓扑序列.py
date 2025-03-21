def add(a, b):
    global idx
    e[idx] = b
    ne[idx] = h[a]
    h[a] = idx
    d[b] += 1
    idx += 1

def bfs():
    hh = 0
    tt = -1
    for i in range(1, n+1):
        if d[i]==0:
            tt += 1
            q.append(i)
    while tt-hh>=0:
        x = q[hh]
        hh += 1
        i = h[x]
        while i!=-1:
            j = e[i]
            d[j] -= 1
            if d[j]==0:
                tt += 1
                q.append(j)
            i = ne[i]
    return tt == n-1

if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    N = int(1e6 + 10)
    e = [0]*m
    ne = [0]*m
    idx = 0
    h = [-1]*(n+1)
    d = [0]*(n+1)
    for _ in range(m):
        a, b = list(map(int, input().split()))
        add(a, b)

    q = []
    if bfs():
        for tmp in q:
            print(tmp, end=' ')
    else:
        print(-1)