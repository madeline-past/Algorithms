if __name__ == '__main__':

    N, V = list(map(int, input().split()))
    v = [None]
    w = [None]
    for _ in range(N):
        v_, w_ = list(map(int, input().split()))
        v.append(v_)
        w.append(w_)

    f = [0]*(V+1)
    for i in range(1, N+1):
        for j in range(V, v[i]-1, -1):
            f[j] = max(f[j], f[j-v[i]] + w[i])
    print(f[V])