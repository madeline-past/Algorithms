n, k = map(int, input().split())
a = list(map(int, input().split()))
N = int(1e6 + 10)
queue = [0] * N
tt = -1
hh = 0

# 和单调栈不一样，滑动窗口里的单调队列不能直接存储数，而是要存储数在原数组中的位置下标，只有这样才能判断队头元素有没有超出窗口范围
# min
for i in range(n):
    x = a[i]
    if tt >= hh  and queue[hh] < i - k + 1:
        hh += 1
    while tt >= hh  and a[queue[tt]] >= x:
        tt -= 1
    tt += 1
    queue[tt] = i
    if i+1 >= k :
        print(a[queue[hh]], end=' ')

print()
tt = -1
hh = 0

# max
for i in range(n):
    x = a[i]
    if tt >= hh  and queue[hh] < i - k + 1:
        hh += 1
    while tt >= hh  and a[queue[tt]] <= x:
        tt -= 1
    tt += 1
    queue[tt] = i
    if i+1 >= k :
        print(a[queue[hh]], end=' ')