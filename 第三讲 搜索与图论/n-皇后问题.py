def dfs(u):
    if u == n:
        for _ans in ans:
            for x in _ans:
                print(x, end='')
            print()
        print()
        return
    for i in range(n):
        if col[i] and dia[n-i+u] and udia[i+u]:
            ans[u][i] = 'Q'
            col[i] = dia[n-i+u] = udia[i+u] = False
            dfs(u + 1)
            col[i] = dia[n-i+u] = udia[i+u] = True
            ans[u][i] = '.'

if __name__ == '__main__':
    n = int(input())
    ans = [['.']*n for _ in range(n)]
    col = [True]*n
    dia = [True]*2*n
    udia = [True]*2*n
    dfs(0)