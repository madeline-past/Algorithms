def add_head(x):
    global head, ne, e, idx
    ne.append(head)
    e.append(x)
    head = idx
    idx += 1

def add_k(k, x):
    global head, ne, e, idx
    e.append(x)
    ne.append(ne[k-1])
    ne[k-1] = idx
    idx += 1

def delete(k):
    global ne, head
    if k:
        ne[k-1] = ne[ne[k-1]]
    else:
        head = ne[head]

n = int(input())
e = []
ne = []
head = -1
idx = 0

for _ in range(n):
    op = input().split()
    if op[0] == 'H':
        add_head(op[1])
    elif op[0] == 'D':
        delete(int(op[1]))
    else:
        add_k(int(op[1]), int(op[2]))

pt = head
while pt != -1:
    print(e[pt], end=' ')
    pt = ne[pt]