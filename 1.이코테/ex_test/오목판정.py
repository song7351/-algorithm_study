test_case = int(input())

def check():
    for i in range(N):
        for j in range(N):
            if board[i][j] == 'o':
                for di,dj in [(-1,1),(0,1),(1,1),(1,0)]:
                    cnt = 1
                    for k in range(1,5):
                        ni = i + di*k
                        nj = j + dj*k
                        if 0<= ni < N and 0<= nj <N and board[ni][nj] == 'o':
                            cnt += 1
                        else:
                            break
                    if cnt == 5:
                        return True
    return False

for tc in range(1, test_case+1):
    N = int(input())
    board = [list(map(str, input())) for _ in range(N)]
    #print(board)
    ans = 'NO'
    if check():
        ans = 'YES'
    print(f"#{tc} {ans}")