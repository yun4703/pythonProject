N, M, K = map(int, input().split())
num = list(map(int, input().split()))
num.sort()

sum = 0
cnt = 0
ln = 0

while True:
    value = num[-1]
    sum += value
    cnt += 1
    ln += 1

    if cnt == K:
        value = num[-2]
        cnt = 0
        sum += value
        ln += 1

    if ln == M:
        print(sum)
        break
