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

if __name__ == '__main__':
    n = int(input())
    # q = [int(i) for i in input().split()]
    q = list(map(int, input().split()))
    quick_sort(q, 0, n-1)
    # for i in range(n):
    #     # print(f'{q[i]}',end=' ')
    #     print('{}'.format(q[i]),end=' ')
    print(' '.join(list(map(str, q))))