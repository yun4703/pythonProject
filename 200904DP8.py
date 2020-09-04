n = int(input())
a = list(map(int, input().split()))
d = [1 for _ in range(n)]
v = [-1 for _ in range(n)]
ans = []
for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            if d[j] + 1 > d[i]:
                d[i] = d[j] + 1
                v[i] = j
mx = max(d)


def go(p):
    if p == -1:
        return

    ans.append(a[p])
    go(v[p])


go(d.index(mx))
ans.reverse()
ans = list(map(str, ans))
print(mx)
print(' '.join(ans))