def quick_sort(q, l, r, k):
    if l >= r:
        return q[k]
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
    if j < k:
        return quick_sort(q, j+1, r, k)
    else:
        return quick_sort(q, l, j, k)

if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    q = list(map(int, input().split()))
    print(str(quick_sort(q, 0, n-1, k-1)))