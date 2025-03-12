stack = [None] * int(1e5 + 10)
tt = 0

def push(x):
    global tt
    tt += 1
    stack[tt] = x

def pop():
    global tt
    tt -= 1

def empty():
    if tt == 0:
        print("YES")
    else:
        print("NO")

def query():
    print(stack[tt])

n = int(input())
for _ in range(n):
    op = input().split()
    if op[0] == 'push':
        push(int(op[1]))
    elif op[0] == 'pop':
        pop()
    elif op[0] == 'empty':
        empty()
    elif op[0] == 'query':
        query()
    else:
        raise NotImplementedError