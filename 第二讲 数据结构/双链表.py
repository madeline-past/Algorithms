def add_right(k, x):
    global e, l, r, idx
    e.append(x)
    l.append(k)
    r.append(r[k])
    l[r[k]] = idx
    r[k] = idx
    idx += 1

def add_left(k, x):
    add_right(l[k], x)

def remove(k):
    global e, l, r, idx
    r[l[k]] = r[k]
    l[r[k]] = l[k]

n = int(input())
e = [None, None]
l = [None, 0]
r = [1, None]
idx = 2

for _ in range(n):
    op = input().split()
    if op[0] == 'IR':
        add_right(int(op[1])+1, int(op[2]))
    elif op[0] == 'IL':
        add_left(int(op[1])+1, int(op[2]))
    elif op[0] == 'R':
        add_left(1, int(op[1]))
    elif op[0] == 'L':
        add_right(0, int(op[1]))
    elif op[0] == 'D':
        remove(int(op[1])+1)
    else:
        raise NotImplementedError

pt = r[0]
while pt != 1:
    print(e[pt], end=' ')
    pt = r[pt]