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

q = list(map(int, input().split()))