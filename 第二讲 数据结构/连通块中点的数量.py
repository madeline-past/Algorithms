def find(x):
    if(p[x] != x):
        p[x] = find(p[x])
    return p[x]

if __name__ == '__main__':
    n, m = map(int, input().split())
    p = [i for i in range(n+1)]
    cnt = [1 for _ in range(n+1)]
    for _ in range(m):
        op = input().split()
        if op[0] == 'C':
            if find(int(op[1])) != find(int(op[2])):
                cnt[find(int(op[2]))] += cnt[find(int(op[1]))]
            p[find(int(op[1]))] = find(int(op[2]))
        elif op[0] == 'Q1':
            if find(int(op[2])) == find(int(op[1])):
                print('Yes')
            else:
                print('No')
        else:
            print(cnt[find(int(op[1]))])