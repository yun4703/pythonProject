n = int(input())
a = list(map(int , input().split()))
d = [0 for _ in range(n)]
d[0] = a[0]
for i in range(1, n):
    if d[i-1]+a[i] > a[i]:
        d[i] = d[i-1]+a[i]
    else:
        d[i] = a[i]


print(max(d))