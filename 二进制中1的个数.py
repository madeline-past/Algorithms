def lowbit(x):
    return x & -x


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    for x in a:
        ans = 0
        while x:
            x -= lowbit(x)
            ans += 1
        print(ans, end=' ')