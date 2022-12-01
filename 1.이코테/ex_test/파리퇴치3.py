test_case = int(input())

for tc in range(1, test_case+1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    di = [-1,-1,0,1,1,1,0,-1]
    dj = [0,1,1,1,0,-1,-1,-1]

    ans = 0

    for i in range(N):
        for j in range(N):
            c = board[i][j]
            p = board[i][j]
            for k in range(1, M):
                for m in range(8):
                    ni = i + di[m]*k
                    nj = j + dj[m]*k
                    if 0<= ni <N and 0<= nj < N:
                        if m%2 == 0:
                            p += board[ni][nj]
                        else:
                            c += board[ni][nj]
            ans = max(ans, p, c)

    print(f'#{tc} {ans}')