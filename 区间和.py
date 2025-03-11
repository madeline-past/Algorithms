def quick_sort(q, l, r):
    if l >= r:
        return
    i = l-1
    j = r+1
    x = q[i+j >> 1]
    while(i < j):
        i += 1
        while q[i] < x:
            i += 1
        j -=1
        while q[j] > x:
            j -=1
        if(i < j):
            q[i], q[j] = q[j], q[i]
    
    quick_sort(q, l, j)
    quick_sort(q, j+1, r)


def unique(q):
    ans = []
    for i, x in enumerate(q):
        if i == 0 or q[i-1] != x:
            ans.append(x)
    return ans


def find(q, x):
    l = 0
    r = len(q)
    while l < r:
        mid = l + r >>1
        if q[mid] >= x:
            r = mid
        else:
            l = mid + 1
    return l


if __name__ == '__main__':
    # N = 3e5 + 100
    n, m = map(int, input().split())
    add = []
    query = []
    alls = []
    for _ in range(n):
        x, c = map(int, input().split())
        add.append([x, c])
        alls.append(x)
    for _ in range(m):
        l, r = map(int, input().split())
        query.append([l, r])
        alls.append(l)
        alls.append(r)
    
    quick_sort(alls, 0, n + 2*m - 1)
    sorted = unique(alls)
    a = [0] * len(sorted)

    for x, c in add:
        idx = find(sorted, x)
        a[idx] += c
    s = [0]
    sum = 0
    for x in a:
        sum += x
        s.append(sum)

    for l, r in query:
        kl = find(sorted, l)
        kr = find(sorted, r)
        kl +=1
        kr +=1
        res = s[kr] - s[kl-1]
        print(res)