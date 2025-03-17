def main():
    n, m, x = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    i = 0
    j = m-1
    while i < n and j >= 0:
        if a[i] + b[j] > x:
            j -= 1
        elif a[i] + b[j] == x:
            print(f"{i} {j}")
            break
        else:
            i += 1

if __name__ == '__main__':
    main()