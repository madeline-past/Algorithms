from collections import defaultdict

def spfa():
    st = [False]*(n+1)
    dist = [0]*(n+1)
    cnt = [0]*(n+1)
    q = []
    hh = 0
    tt = -1
    for i in range(1, n+1):
        st[i] = True
        tt += 1
        q.append(i)
    while tt-hh>=0:
        x = q[hh]
        hh += 1
        st[x] = False
        for y, w in g[x]:
            if dist[y] > dist[x] + w:
                dist[y] = dist[x] + w
                cnt[y] = cnt[x] + 1
                if cnt[y] >= n:
                    print('Yes')
                    return
                if not st[y]:
                    tt += 1
                    q.append(y)
                    st[y] = True

    print('No')



if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    g = defaultdict(list)
    for _ in range(m):
        x, y, w = list(map(int, input().split()))
        g[x].append([y, w])

    spfa()