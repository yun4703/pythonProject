n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))
a = [0]+a

d = [[0 for _ in range(3)] for _ in range(n+1)]

for i in range(1, n+1):
    d[i][0] = max(d[i-1][0],d[i-1][1], d[i-1][2])
    d[i][1] = d[i-1][0] + a[i]
    d[i][2] = d[i-1][1] + a[i]

mx = 0
for i in d:
    mx = max(mx, max(i))

print(mx)