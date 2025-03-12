def insert(b, l, r, c):
    b[l] += c
    b[r+1] -= c

if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = [0] * (n+1)
    for i, x in enumerate(a):
        insert(b, i, i, x)
    for _ in range(k):
        l, r, c = list(map(int, input().split()))
        insert(b, l-1, r-1, c)
    sum = 0
    for i in range(n):
        sum += b[i]
        print(sum, end=' ')


