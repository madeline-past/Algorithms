N = int(1e5 + 10)
a = [[0]*26 for _ in range(N)]
idx = 0
cnt = [0]*N

def insert(str):
    global a, idx, cnt
    p = 0
    for c in str:
        x = ord(c) - ord('a')
        if a[p][x]:
            p = a[p][x]
        else:
            idx += 1
            a[p][x] = idx
            p = idx
    cnt[p] += 1

def query(str):
    global a, idx, cnt
    p = 0
    for c in str:
        x = ord(c) - ord('a')
        if a[p][x]:
            p = a[p][x]
        else:
            return 0
    return cnt[p]

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        op = input().split()
        if op[0] == 'I':
            insert(op[1])
        else:
            print(query(op[1]))