num = float(input())
# neg = False
# if num <0:
#     num = -num
#     neg = True
l = -10000
r = 10000
while r-l >= 1e-8:
    mid = (r+l) /2
    if mid**3 < num:
        l = mid
    else:
        r = mid

# if neg:
#     l = -l
print(format(l, '.6f'))