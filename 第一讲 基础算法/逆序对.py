def count_inversions(q, l, r):
    if l >= r:
        return 0
    mid = l+r >>1

    count = 0
    count += count_inversions(q, l, mid)
    count += count_inversions(q, mid+1, r)

    # 从小到大排序
    i = l
    j = mid + 1
    tmp = []
    while i <= mid and j <= r:
        if q[i] <= q[j]:
            tmp.append(q[i])
            i +=1
        else:
            tmp.append(q[j])
            j +=1
            count += (mid - i + 1)
    while i <= mid:
        tmp.append(q[i])
        i +=1
    while j <= r:
        tmp.append(q[j])
        j +=1

    for k, i in enumerate(range(l,r+1)):
        q[i] = tmp[k]
    
    return count

if __name__ == '__main__':
    n = int(input())
    q = list(map(int, input().split()))
    print(f"{count_inversions(q, 0, n-1)}")


