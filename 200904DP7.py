n = int(input())
a = list(map(int, input().split()))
d = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            if d[j]+1 > d[i]:
                d[i] = d[j] + 1

print(max(d))