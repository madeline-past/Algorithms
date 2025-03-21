def dijkstra():
    st = [True]*(n+1)
    dist = [inf]*(n+1)
    dist[1] = 0

    for _ in range(1, n+1):
        t = -1
        for i in range(1, n+1):
            if st[i] and (t == -1 or dist[t] > dist[i]):
                t = i
        st[t] = False

        for i in range(1, n+1):
            dist[i] = min(dist[i], dist[t] + d[t][i])

    if dist[n] == inf:
        return -1
    else:
        return dist[n]

if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    N = int(1e6 + 10)
    inf = float("inf")
    d = [[inf]*(n+1) for _ in range(n+1)]
    for _ in range(m):
        a, b, c = list(map(int, input().split()))
        d[a][b] = min(d[a][b], c)

    print(dijkstra())