def add(a, b):
    global idx
    e[idx] = b
    ne[idx] = h[a]
    h[a] = idx
    idx += 1

def bfs():
    global flag
    q = [1]
    st[1] = False
    tt = hh =0
    while tt-hh>=0:
        # print(q[hh:])
        x = q[hh]
        hh += 1
        i = h[x]
        if x == n:
            print(distance[x])
            flag = True
            return
        while i!=-1:
            j = e[i]
            if st[j]:
                st[j] = False
                distance[j] = distance[x] + 1
                q.append(j)
                tt += 1
            i = ne[i]

if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    N = int(1e6 + 10)
    e = [0]*m
    ne = [0]*m
    idx = 0
    h = [-1]*(n+1)
    for _ in range(m):
        a, b = list(map(int, input().split()))
        add(a, b)
    st = [True]*(n+1)
    distance = [0]*(n+1)
    flag = False
    bfs()
    if not flag:
        print(-1)