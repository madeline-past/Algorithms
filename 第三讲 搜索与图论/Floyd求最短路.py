def floyd():
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                g[i][j] = min(g[i][j], g[i][k] + g[k][j])

if __name__ == '__main__':
    n, m, k = list(map(int, input().split()))

    g = [[float("inf")]*(n+1) for _ in range(n+1)]
    for i in range(n+1):
        g[i][i] = 0

    for _ in range(m):
        x, y, w = list(map(int, input().split()))
        g[x][y] = min(g[x][y], w)

    floyd()

    for _ in range(k):
        x, y = list(map(int, input().split()))
        print(g[x][y] if g[x][y] is not float("inf") else "impossible")