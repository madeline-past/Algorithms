def dfs(u):
    if u == n:
        for x in num:
            print(x, end=' ')
        print()
        return
    for i in range(1, n+1):
        if flag[i]:
            num[u] = i
            flag[i] = False
            dfs(u + 1)
            flag[i] = True


if __name__ == '__main__':
    n = int(input())
    num = [0]*n
    flag = [True]*(n+1)
    dfs(0)