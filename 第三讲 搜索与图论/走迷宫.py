def bfs():
    q = [[0, 0]]
    hh = tt = 0
    st = [[True]*m for _ in range(n)]
    st[0][0] = False
    distance = [[0]*m for _ in range(n)]
    while tt - hh >= 0:
        point = q[hh]
        hh += 1
        if point == [n-1, m-1]:
            print(distance[point[0]][point[1]])
            return
        sxzy = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        for i in range(4):
            next = [point[k] + sxzy[i][k] for k in range(2)]
            if next[0]>=0 and next[0]<n and next[1]>=0 and next[1]<m and g[next[0]][next[1]]!=1 and st[next[0]][next[1]]:
                tt += 1
                q.append(next)
                st[next[0]][next[1]] = False
                distance[next[0]][next[1]] = distance[point[0]][point[1]] + 1
        # print(q[hh:])

if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    g = []
    for _ in range(n):
        tmp = list(map(int, input().split()))
        g.append(tmp)
    bfs()
