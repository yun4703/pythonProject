n = int(input())
a = list(map(int , input().split()))
d1 = [0 for _ in range(n)]
d2 = [0 for _ in range(n)]

for i in range(n):
    d1[i] = 1
    for j in range(i):
        if a[i] > a[j] and d1[j]+1 > d1[i]:
            d1[i] = d1[j] + 1


for i in range(n-1,-1,-1):
    d2[i] = 1
    for j in range(i, n):
        if a[i] > a[j] and d2[j]+1 > d2[i]:
            d2[i] = d2[j] + 1

mx = 0
for i in range(len(d1)):
    if d1[i]+d2[i] - 1 > mx:
        mx = d1[i]+d2[i] - 1

print(mx)