def bellman_ford():
    dist = [float("inf")]*(n+1)
    dist[1] = 0
    for _ in range(k):
        backup = dist.copy()
        for x, y, w in g:
            dist[y] = min(dist[y], backup[x] + w)
            print(dist)

    if dist[n] == float("inf"):
        print("impossible")
    else:
        print(dist[n])

if __name__ == '__main__':
    n, m, k = list(map(int, input().split()))
    g = []
    for _ in range(m):
        tmp = list(map(int, input().split()))
        g.append(tmp)
    bellman_ford()