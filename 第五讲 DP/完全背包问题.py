if __name__ == '__main__':

    n, m = list(map(int, input().split()))
    v = [None]
    w = [None]
    for _ in range(n):
        v_, w_ = list(map(int, input().split()))
        v.append(v_)
        w.append(w_)

    # f = [[0]*(m+1) for _ in range(n+1)]
    # # # pususuanfa
    # # for i in range(1, n+1):
    # #     for j in range(1, m+1):
    # #         for k in range(0, j//v[i]+1):
    # #             f[i][j] = max(f[i][j], f[i-1][j-k*v[i]] + k*w[i])

    # for i in range(1, n+1):
    #     for j in range(1, m+1):
    #         f[i][j] = f[i-1][j]
    #         if j >= v[i]:
    #             f[i][j] = max(f[i][j], f[i][j-v[i]]+w[i])

    # print(f[n][m])

    f = [0]*(m+1)
    for i in range(1, n+1):
        for j in range(v[i], m+1):
            f[j] = max(f[j], f[j-v[i]]+w[i])

    print(f[m])