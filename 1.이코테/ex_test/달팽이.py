test_case = int(input())

for tc in range(1, test_case+1):
    N = int(input())
    board = [[0]*N for _ in range(N)]
    i, j, num = 0, -1, 0
    while num < N**2:
        for di,dj in [(0,1),(1,0),(0,-1),(-1,0)]:
            while True:
                ni = i + di
                nj = j + dj
                if 0<= ni < N and 0<=nj<N and board[ni][nj] == 0:
                    i,j = ni, nj
                    num += 1
                    board[i][j] = num
                else:
                    break
            if num == N**2:
                break

    print(f"#{tc}")
    for i in board:
        print(*i)