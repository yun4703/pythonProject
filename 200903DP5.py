T = int(input())

for _ in range(T):
    n = int(input())
    a = []
    for _ in range(2):
        a.append([0] + list(map(int, input().split())))
    stk = list(map(list, zip(*a)))
    d = [[0 for _ in range(3)] for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(3):
            if j == 0:
                d[i][j] = max(d[i-1][0], d[i-1][1], d[i-1][2])
            elif j == 1:
                d[i][j] = max(d[i-1][0], d[i-1][2]) + stk[i][0]
            else:
                d[i][j] = max(d[i-1][0], d[i-1][1]) + stk[i][1]

    mx = 0
    for i in d:
        mx = max(mx, max(i))

    print(mx)