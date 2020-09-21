N, M = map(int, input().split())
board = []
for i in range(N):
    board.append(list(map(int, input().split())))

mn = 0
for i in board:
    tmp = min(i)
    if tmp > mn:
        mn = tmp

print(mn)