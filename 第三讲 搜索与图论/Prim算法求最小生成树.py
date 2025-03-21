def prim():
    dist = [float("inf")]*(n+1)
    # dist[1] = 0

    st = [True]*(n+1)
    # st[1] = False

    res = 0
    for _ in range(n):
        t = -1
        for i in range(1, n+1):
            if st[i] and (t==-1 or dist[t]>dist[i]):
                t = i

        if t!=1 and dist[t]==float("inf"):
            print("impossible")
            return
        
        st[t] = False
        if t!=1:
            res += dist[t]

        for i in range(1, n+1):
            dist[i] = min(dist[i], g[t][i])
    print(res)

if __name__ == '__main__':

    n, m = list(map(int, input().split()))

    g = [[float("inf")]*(n+1) for _ in range(n+1)]
    for _ in range(m):
        x, y, w = list(map(int, input().split()))
        g[x][y] = g[y][x] = min(g[x][y], w)
    
    prim()