"""
https://www.acmicpc.net/problem/3190
뱀 게임
사과를 먹으면 머리만 움직이고 없으면 꼬리가 움직인다.
뱀의 길이는 1 이다. 뱀은 처음에 오른쪽을 향한다.
1줄: 보드크기 N
2줄: 사과개수 K
K줄: 사과위치(행,열)
K+1줄: 뱀방향전환 횟수 L
L줄: X초 LD(왼오)방향
"""

N = int(input())
board = [[0]* N for _ in range(N)]
K = int(input())
for i in range(K):
    x,y = map(int,input().split())  # 사과
    board[x-1][y-1] = 1
L = int(input())

direction = []
for i in range(L):
    x,y = input().split()
    x = int(x)
    direction.append([x,y]) # x초에는 y방향으로 꺽어라
direction.append([10000,'D']) # 마지막 방향에서는 계속해서 직진해라

snake = [[0,0]]     # 꼬리 ~ 머리
board[0][0] = 3     # 뱀위치는 3
tail = snake[0]     # 꼬리위치
head = snake[-1]    # 머리위치

di = [-1,0,1,0]     # 상 좌 하 우
dj = [0,-1,0,1]
d = 3               # 현재 방향

cnt = 0             # 초
flag = 0
for i in range(L+1):
    for j in range(direction[i][0]-cnt):
        tail = snake[0]  # 꼬리위치
        head = snake[-1]  # 머리위치
        ni = head[0] + di[d]
        nj = head[1] + dj[d]
        cnt += 1
        if 0<= ni < N and 0<= nj <N:
            snake.append([ni,nj])
            if board[ni][nj] == 0:              # 사과가 없다면
                board[tail[0]][tail[1]] = 0     # 꼬리를 땡겨라
                snake.pop(0)
            elif board[ni][nj] == 3:            # 몸통이랑 접촉하면 끝
                flag = 1
                break
            board[ni][nj] = 3                   # 사과 또는 아무것도 없다면 진행
        else:                                   # 벽이랑 접촉해도 끝
            flag = 1
            break
    if flag == 1:
        break

    if direction[i][1] == 'L':                  # 방향을 왼쪽으로
        d += 1
        if d == 4:
            d = 0
    else:                                       # 방향을 오른쪽으로
        d -= 1
        if d == -1:
            d = 4

print(cnt)