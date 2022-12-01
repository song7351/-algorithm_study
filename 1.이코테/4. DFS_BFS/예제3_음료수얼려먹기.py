"""
N * M 얼음틀
구멍: 0
칸막이: 1
0상하좌우에 0있으면 한덩어리로 취급
그래서 0덩어리의 총 개수는?
"""
def dfs(x,y):
    board[x][y] = 3                     # 방문했다는 의미로 3
    for k in range(4):                  # 4방향 주변에 0이 있나요?
        ni = x + di[k]
        nj = y + dj[k]
        if 0<= ni < N and 0<= nj< M:
            if board[ni][nj] == 0:      # 0이 있다면
                board[ni][nj] = 3       # 방문처리 해주시고
                dfs(ni,nj)              # 해당 좌표로 주변탐색 반복

N, M = map(int, input().split())
board = [list(map(int, input())) for _ in range(N)]

di = [-1,1,0,0]
dj = [0,0,-1,1]

ans = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            dfs(i,j)
            ans += 1

print(ans)