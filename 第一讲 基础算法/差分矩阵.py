def insert(b, x1, y1, x2, y2, c):
    b[x1][y1] += c
    b[x2+1][y1] -= c
    b[x1][y2+1] -= c
    b[x2+1][y2+1] += c

if __name__ == '__main__':
    r, c, k = map(int, input().split())
    b = [[0]*(c+1) for _ in range(r+1)]
    a = [list(map(int, input().split())) for _ in range(r)]

    for i in range(r):
        for j in range(c):
            insert(b, i, j, i, j, a[i][j])
    for _ in range(k):
        x1, y1, x2, y2, val = list(map(int, input().split()))
        insert(b, x1-1, y1-1, x2-1, y2-1, val)

    sum = [[0]*(c+1) for _ in range(r+1)]
    for i in range(1, r+1):
        for j in range(1, c+1):
            sum[i][j] = sum[i-1][j] + sum[i][j-1] - sum[i-1][j-1] + b[i-1][j-1]
            print(sum[i][j], end=' ')
        print()
