from collections import defaultdict
import heapq

def dijkstra():
    st = [True]*(n+1)
    dist = [float("inf")]*(n+1)
    dist[1] = 0
    q = []
    heapq.heappush(q, [0, 1])
    while len(q):
        d, x = heapq.heappop(q)
        if not st[x]:
            continue
        st[x] = False
        for j, d in g[x]:
            if dist[j] > dist[x] + d:
                dist[j] = dist[x] + d
                heapq.heappush(q, [dist[j], j])
    print(dist[n] if dist[n] is not float("inf") else -1)

if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    g = defaultdict(list)
    for _ in range(m):
        a, b, c = list(map(int, input().split()))
        g[a].append([b, c])
    dijkstra()