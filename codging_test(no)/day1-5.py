from collections import deque
N, M = map(int, input().split())
a, b, d = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

check = [[False for _ in range(M)] for _ in range(N)]

q = deque()
q.append([a, b, d])
cnt = 1
check[a][b] = True

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while q:
    x, y, d = q.popleft()
    for i in range(4):
        d -= 1
        nx = x+dx[d]
        ny = y+dy[d]
        if 0 <= nx < N and 0 <= ny < M:
            if check[nx][ny] is False and board[nx][ny] != 1:
                check[nx][ny] = True
                q.append([nx, ny, dx.index(dx[d])])
                cnt += 1

print(cnt)