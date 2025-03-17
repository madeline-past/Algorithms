# 并查集好像并不关心数据的具体内容，只需要数据的索引，而它最主要的两个功能————合并和查询，也是只需要数据的索引就能完成

# N = int(1e5 + 10)
# p = [i for i in range(N)]

def find(x):
    if(p[x] != x):
        p[x] = find(p[x])
    return p[x]

if __name__ == '__main__':
    n, m = map(int, input().split())
    p = [i for i in range(n+1)]
    for _ in range(m):
        op = input().split()
        if op[0] == 'M':
            p[find(int(op[1]))] = find(int(op[2]))
        else:
            if find(int(op[2])) == find(int(op[1])):
                print('Yes')
            else:
                print('No')