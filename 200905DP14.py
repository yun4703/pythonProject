n = int(input())
d = [0 for _ in range(n+1)]
for i in range(1,n+1):
    d[i] = i
    for j in range(1,i):
        if j*j <= i:
            if d[i] > d[i-j*j] + 1:
                d[i] = d[i - j * j] + 1

print(d[n])


#정답 , 위에꺼 시간 초과

n = int(input())
d = [0]*(n+1)
for i in range(1, n+1):
    d[i] = i
    j = 1
    while j*j <= i:
        if d[i] > d[i-j*j]+1:
            d[i] = d[i-j*j]+1
        j += 1
print(d[n])