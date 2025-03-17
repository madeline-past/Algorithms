# def main():
#     n, m = list(map(int, input().split()))
#     a = list(map(int, input().split()))
#     b = list(map(int, input().split()))
#     i = j = -1
#     while i < n-1 and j < m-1:
#         i += 1
#         j += 1
#         if a[i] != b[j]:
#             while j < m-1:
#                 j += 1
#                 if a[i] == b[j]:
#                     break

#     if i == n-1 and a[i] == b[j]:
#         print("Yes")
#     else:
#         print("No")

def main():
    n, m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    i = j = 0
    while i < n and j < m:
        if a[i] == b[j]:
            i += 1
            j += 1
        else:
            j += 1

    if i == n:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()