import sys

N,M,B = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
time_ans = int(1e9)
height_ans = 0
for tmp_height in range(0,256+1):
    tmp_time = 0
    minus, plus = 0,0
    for i in range(N):
        for j in range(M):
            if board[i][j] > tmp_height:
                minus += board[i][j] - tmp_height
            elif board[i][j] < tmp_height:
                plus += tmp_height - board[i][j]
    if plus > B + minus:
        continue
    else:
        tmp_time += minus*2 + plus
        if tmp_time < time_ans:
            time_ans = tmp_time
            height_ans = tmp_height

print(time_ans, height_ans)
