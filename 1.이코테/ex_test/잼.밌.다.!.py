"""
1은흑돌
-1은 백돌
"""
test_case = int(input())

for tc in range(1, test_case+1):
    N, M = map(int, input().split())
    board = [[0]*N for _ in range(N)]
    board[N//2][N//2], board[N//2 - 1][N//2 - 1] = -1, -1
    board[N//2][N//2 - 1], board[N//2 - 1][N//2] = 1, 1
    for _ in range(M):
        x,y,c = map(int, input().split())
        x,y = x-1, y-1
        if c == 2:
            c = -1
        board[x][y] = c
        for di, dj in [(1,1),(1,0),(1,-1),(0,1),(0,-1),(-1,1),(-1,0),(-1,-1)]:
            tmp_lst = []
            for k in range(1,N):
                ni = x + di*k
                nj = y + dj*k
                if 0<= ni < N and 0<= nj <N:
                    if board[ni][nj] == -c:
                        tmp_lst.append((ni,nj))
                    elif board[ni][nj] == c:
                        for tx,ty in tmp_lst:
                            board[tx][ty] = c
                        break
                    else:
                        break
                else:
                    break
    w_cnt = 0
    b_cnt = 0

    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                b_cnt += 1
            elif board[i][j] == -1:
                w_cnt += 1

    print(f"#{tc} {b_cnt} {w_cnt}")