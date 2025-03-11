if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    N = 1e5 + 10
    s = [0] * int(N)
    j = 0
    ans = 0
    for i in range(n):
        s[a[i]] += 1
        while s[a[i]] > 1:
            s[a[j]] -= 1
            j += 1
        ans = max(ans, i-j+1)
    print(ans)

        