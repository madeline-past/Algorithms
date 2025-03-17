n = int(input())
q = list(map(int, input().split()))
N = int(1e5 + 10)
stack = [0] * N
tt = 0
for i in range(n):
    x = q[i]
    while tt and stack[tt] >= x:
        tt -= 1
    if tt:
        print(stack[tt], end=' ')
    else:
        print("-1", end=' ')
    tt += 1
    stack[tt] = x
