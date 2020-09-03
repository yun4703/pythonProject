N = int(input())
d = [[0 for _ in range(2)] for _ in range(91)]
d[1][1] = 1

for i in range(2, N+1):
    for j in range(2):
        if j == 0:
            d[i][j] = d[i-1][0] + d[i-1][1]
        else:
            d[i][j] = d[i-1][0]

print(sum(d[N]))