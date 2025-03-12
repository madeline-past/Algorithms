def quick_sort(q, l, r):
    if l >= r:
        return
    i = l-1
    j = r+1
    x = q[i+j >> 1][0]
    while(i < j):
        i += 1
        while q[i][0] < x:
            i += 1
        j -=1
        while q[j][0] > x:
            j -=1
        if(i < j):
            q[i], q[j] = q[j], q[i]
    
    quick_sort(q, l, j)
    quick_sort(q, j+1, r)

if __name__ == '__main__':
    n = int(input())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))
    # st = [x[0] for x in a]
    quick_sort(a, 0, n-1)
    x = a[0]
    # ans = []
    ans = 0
    for next in a[1:]:
        st, ed = next
        if ed <= x[1]:
            pass
        else:
            if st <= x[1]:
                x[1] = ed
            else:
                # ans.append(x)
                ans += 1
                x = next
    print(ans +1)



    