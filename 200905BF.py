n = int(input())
m = int(input())
if m > 0:
    non_num = list(map(int, input().split()))
else:
    non_num = []

mn = abs(n - 100)

for i in range(1000001):
    a = list(str(i))
    a = list(map(int, a))
    temp = True
    for j in non_num:
        if j in a:
            temp = False
            break

    if temp:
        cnt = abs(n-i)
        if cnt+len(a) < mn:
            mn = cnt+len(a)


print(mn)
