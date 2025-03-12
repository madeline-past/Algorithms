def merge_sort(q, l ,r):
    if l >= r:
        return
    mid = l+r >> 1
    merge_sort(q, l, mid)
    merge_sort(q, mid+1, r)

    i = l
    j = mid + 1
    tmp = []
    while i <= mid and j <= r:
        if q[i] < q[j]:
            tmp.append(q[i])
            i +=1
        else:
            tmp.append(q[j])
            j +=1
    while i <= mid:
        tmp.append(q[i])
        i +=1
    while j <= r:
        tmp.append(q[j])
        j +=1

    for k, i in enumerate(range(l,r+1)):
        q[i] = tmp[k]

if __name__ == '__main__':
    n = int(input())
    q = list(map(int, input().split()))
    merge_sort(q, 0, n-1)
    print(' '.join(list(map(str, q))))
