if __name__ == '__main__':

    n, m = list(map(int, input().split()))
    v = [None]
    w = [None]
    # s = [None]
    cnt = 0
    for _ in range(n):
        vi, wi, si = list(map(int, input().split()))
        k = 1

        while si>=k:
            cnt +=1
            si -= k
            v_ = vi * k
            w_ = wi * k
            # s_ = k

            v.append(v_)
            w.append(w_)
            # s.append(s_)
        if si>0:
            cnt += 1
            v_ = vi * si
            w_ = wi * si
            v.append(v_)
            w.append(w_)

    n = cnt
    f = [0]*(m+1)
    for i in range(1, n+1):
        for j in range(m, v[i]-1, -1):
            f[j] = max(f[j], f[j-v[i]]+w[i])

    print(f[m])