from collections import defaultdict

def spfa():
    st = [False]*(n+1)
    st[1] = True
    dist = [float("inf")]*(n+1)
    dist[1] = 0

    q = [1]
    tt = hh = 0
    while tt-hh>=0:
        x = q[hh]
        hh += 1
        for y, w in g[x]:
            if dist[y] > dist[x] + w:
                dist[y] = dist[x] + w
                if not st[y]:
                    tt += 1
                    q.append(y)
                    st[y] = True
        st[x] = False
    
    print(dist[n] if dist[n] is not float("inf") else 'impossible')


if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    g = defaultdict(list)
    for _ in range(m):
        x, y, w = list(map(int, input().split()))
        g[x].append([y, w])

    spfa()